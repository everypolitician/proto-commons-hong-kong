	SELECT
		'LC 1' as "CODE",
		'香港島' as "NAME",
		'Hong Kong Island' as "NAME_EN",
		6 as "SEATS",
		'country:hk' as "MS_FB_PARE",
		'country:hk/legislative-council-constituency:lc1' as "MS_FB",
		'Q3248921' as "WIKIDATA",
		ST_Union(a.geometry) as "geometry"
	FROM
		hksar_18_district_boundary as a
	WHERE a."District" IN ('Central & Western', 'Wan Chai', 'Eastern', 'Southern')
UNION
	SELECT
		'LC 2' as "CODE",
		'九龍西' as "NAME",
		'Kowloon West' as "NAME_EN",
		6 as "SEATS",
		'country:hk' as "MS_FB_PARE",
		'country:hk/legislative-council-constituency:lc2' as "MS_FB",
		'Q10879625' as "WIKIDATA",
		ST_Union(a.geometry) as "geometry"
	FROM
		hksar_18_district_boundary as a
	WHERE a."District" IN ('Yau Tsim Mong', 'Sham Shui Po', 'Kowloon City')
UNION
	SELECT
		'LC 3' as "CODE",
		'九龍東' as "NAME",
		'Kowloon East' as "NAME_EN",
		5 as "SEATS",
		'country:hk' as "MS_FB_PARE",
		'country:hk/legislative-council-constituency:lc3' as "MS_FB",
		'Q10879608' as "WIKIDATA",
		ST_Union(a.geometry) as "geometry"
	FROM
		hksar_18_district_boundary as a
	WHERE a."District" IN ('Wong Tai Sin', 'Kwun Tong')
UNION
	SELECT
		'LC 4' as "CODE",
		'新界西' as "NAME",
		'New Territories West' as "NAME_EN",
		9 as "SEATS",
		'country:hk' as "MS_FB_PARE",
		'country:hk/legislative-council-constituency:lc4' as "MS_FB",
		'Q1099862' as "WIKIDATA",
		ST_Union(a.geometry) as "geometry"
	FROM
		hksar_18_district_boundary as a
	WHERE a."District" IN ('Tsuen Wan', 'Tuen Mun', 'Yuen Long', 'Kwai Tsing', 'Islands')
UNION
	SELECT
		'LC 5' as "CODE",
		'新界東' as "NAME",
		'New Territories East' as "NAME_EN",
		9 as "SEATS",
		'country:hk' as "MS_FB_PARE",
		'country:hk/legislative-council-constituency:lc5' as "MS_FB",
		'Q11083612' as "WIKIDATA",
		ST_Union(a.geometry) as "geometry"
	FROM
		hksar_18_district_boundary as a
	WHERE a."District" IN ('North', 'Tai Po', 'Sha Tin', 'Sai Kung')
