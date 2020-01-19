# -*- coding:utf-8 -*-
from __future__ import print_function
from __future__ import division
import arcpy as ap
import arcpy.da as da
from algokit.geo import geohash


def gridsOfPolygon(inputfc, bits, outputfc):
    print('gridsOfPolygon({0},{1},{2})'.format(inputfc, bits, outputfc))
    ext = getExtent(inputfc)
    gridsOfEnvelope(bits, outputfc, *ext)

def autoGeohashesByPolygon(inputfc, numGrid=20):
    ext = getExtent(inputfc)
    return geohash.autoGeohashesByEvelope(numGrid, *ext)

def splitKeyByEnvelope(inputfc,numSplit=20):
    '''
    For Hbase rowkey split
    :return:
    '''
    ext = getExtent(inputfc)
    return geohash.splitKeyByEnvelope(numSplit,*ext)

def gridsOfEnvelope(bits, fc, minlonLimit, maxlonLimit, minlatLimit, maxlatLimit):
    print('gridsOfEnvelope({0},{1},{2},{3},{4},{5})'.format(bits, fc, minlonLimit, maxlonLimit, minlatLimit, maxlatLimit))
    featureList = []
    point = ap.Point()
    array = ap.Array()

    lonSplit, latSplit = geohash.fastFishnet(bits, minlonLimit, maxlonLimit, minlatLimit, maxlatLimit)

    for ilon in range(len(lonSplit) - 1):
        for ilat in range(len(latSplit) - 1):
            minlon = lonSplit[ilon]
            maxlon = lonSplit[ilon + 1]
            minlat = latSplit[ilat]
            maxlat = latSplit[ilat + 1]
            point.X = minlon
            point.Y = minlat
            array.add(point)
            point.X = maxlon
            point.Y = minlat
            array.add(point)
            point.X = maxlon
            point.Y = maxlat
            array.add(point)
            point.X = minlon
            point.Y = maxlat
            array.add(point)
            array.add(array.getObject(0))

            polygon = ap.Polygon(array)
            featureList.append(polygon)
            array.removeAll()

    ap.CopyFeatures_management(featureList, fc)
    ap.DefineProjection_management(fc, ap.SpatialReference(4326))
    addGeohashField(fc, "geohash", bits)


def addGeohashField(fc, fieldName, bits):
    print('addGeohashField({0},{1},{2})'.format(fc, fieldName, bits))
    ap.AddField_management(fc, fieldName, "TEXT", bits)

    with da.UpdateCursor(fc, (fieldName, 'SHAPE@TRUECENTROID')) as cursor:
        for row in cursor:
            row[0] = geohash.getGeohash(bits, *row[1])[0]
            cursor.updateRow(row)


def getExtent(fc):
    print('getExtent({0})'.format(fc))
    minlon = 180
    maxlon = -180
    minlat = 90
    maxlat = -90
    with da.SearchCursor(fc, ('SHAPE@')) as cursor:
        for row in cursor:
            ext = row[0].extent
            if ext.XMin < minlon:
                minlon = ext.XMin
            if ext.XMax > maxlon:
                maxlon = ext.XMax
            if ext.YMin < minlat:
                minlat = ext.YMin
            if ext.YMax > maxlat:
                maxlat = ext.YMax
    return minlon, maxlon, minlat, maxlat


if __name__ == '__main__':
    input_path = r"E:/wk/ArcGISdata/bengbu/bb_fy.shp"
    input_path = r"E:/wk/ArcGISdata/chongqing/cq/chongqing.shp"
    #print autoGeohashesByPolygon(input_path,20)
    print(splitKeyByEnvelope(input_path,20))
    #output_path = r"E:/wk/ArcGISdata/test/geohash1.shp"
    # gridsOfPolygon(input_path,7,output_path)
    # gridsOfEnvelope(1, output_path, -180, 180, -90, 90)
