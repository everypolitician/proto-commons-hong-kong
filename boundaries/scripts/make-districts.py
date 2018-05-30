from shapely.geometry import MultiPolygon  # Polygon,  LinearRing
# import shapely
from shapely.geometry import shape, mapping
from shapely.geometry.polygon import orient
import fiona
import fiona.crs
import fiona.transform


def orient_polygons(shp):
    if shp.geom_type == 'Polygon':
        return orient(shp)
    elif shp.geom_type == 'MultiPolygon':
        oriented_polygons = []
        for polygon in shp:
            oriented = orient_polygons(polygon)
            oriented_polygons.append(oriented)
        return MultiPolygon(oriented_polygons)
    else:
        print('shp is not a Polygon or a MultiPolygon')


def orient_feature(geometry):
    shp = shape(geometry)
    oriented_shp = orient_polygons(shp)
    return mapping(oriented_shp)


def correct_encoding(feature):
    corrections = dict(
        [(u'深水?', u'深水埗'), (u'逸東?', u'逸東邨'), (u'鴨?洲?', u'鴨脷洲邨'),
         (u'鴨?洲北', u'鴨脷洲北'), (u'杏花?', u'杏花邨'), (u'錦?花園', u'錦綉花園'),
         (u'頌?', u'頌栢'), (u'?雅', u'栢雅'), (u'葵盛東?', u'葵盛東邨'),
         (u'葵盛西?', u'葵盛西邨'), (u'牛頭角上?', u'牛頭角上邨'),
         (u'牛頭角下?', u'牛頭角下邨'), (u'葵涌?北', u'葵涌邨北'),
         (u'葵涌?南', u'葵涌邨南'), (u'?業', u'啟業'), (u'禾輋?', u'禾輋邨'),
         (u'?魚涌', u'鰂魚涌'), (u'青衣?', u'青衣邨'), (u'逸東?北', u'逸東邨北'),
         (u'逸東?南', u'逸東邨南'), (u'深水?區', u'深水埗區'), (u'盛褔', u'盛福'),
         (u'屯門市中心', u'屯門巿中心'), (u'頌栢', u'頌柏'), (u'柏架山',u'栢架山')]
    )
    for key in feature['properties']:
        if feature['properties'][key] in corrections:
            corrected = corrections[feature['properties'][key]]
            feature['properties'][key] = corrected
    return feature


def generate_attributes(feature):
    attributes = feature['properties'].copy()
    district = attributes['DISTRICT_E'].replace(' ', '-').replace('&', 'and')
    name = attributes['ENAME'].replace(' ', '-').replace('&', 'and')
    ms_fb_pare = 'country:hk/district:{}'.format(district.lower())
    ms_fb = '{}/constituency:{}'.format(ms_fb_pare, name.lower())
    attributes.update({'MS_FB_PARE': ms_fb_pare, 'MS_FB': ms_fb})

    feature['properties'] = attributes
    return feature


def make_shp(source, output, src_encoding, src_crs, verbose=0):
    """"""
    with fiona.open(source, 'r', encoding=src_encoding, crs=src_crs) as src:
        if verbose:
            print('src crs is {}'.format(src.crs))
            print('src schema is {}'.format(src.schema))

        out_schema = src.schema.copy()
        out_schema['properties'].update({
            'MS_FB_PARE': 'str:100',
            'MS_FB': 'str:100'})

        with fiona.open(output, 'w',
                        encoding='UTF-8',
                        driver='ESRI Shapefile',
                        schema=out_schema,
                        crs=fiona.crs.from_epsg(4326)) as output_shp:

            for f in src:
                f['geometry'] = fiona.transform.transform_geom(src_crs,
                                                               'EPSG:4326',
                                                               f['geometry'])

                f['geometry'] = orient_feature(f['geometry'])

                f = correct_encoding(f)

                # This step could be broken out into separate areas.
                f = generate_attributes(f)

                print(f['id'])
                output_shp.write(f)


if __name__ == '__main__':
    district_constiuencies_src = '../source/GIH3_DC_2015_POLY.shp'
    districts_constituencies_out = '../build/district-constituencies/district-constituencies.shp'

    make_shp(source=district_constiuencies_src,
             output=districts_constituencies_out,
             src_encoding='big5',
             src_crs=fiona.crs.from_epsg(2326),
             verbose=1)
