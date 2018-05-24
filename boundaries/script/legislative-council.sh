#!/bin/bash

ogr2ogr \
	-f 'ESRI Shapefile' \
	-dialect sqlite \
	-sql \@legislative-council.sql \
	-t_srs 'EPSG:4326' \
	../build/legislative-council-consituencies/legislative-council-consituencies.shp \
	../source/hksar_18_district_boundary.shp \
	-lco ENCODING=UTF-8

ogr2ogr \
	 -f 'CSV' \
	 ../build/legislative-council-consituencies/legislative-council-consituencies.csv \
	 ../build/legislative-council-consituencies/legislative-council-consituencies.shp \
