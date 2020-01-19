# -*- coding:utf-8 -*-
from __future__ import print_function
from __future__ import division
import arcpy as ap
import GeohashTools as ght

def main():
    input_path = ap.GetParameterAsText(0)
    output_path = ap.GetParameterAsText(1)
    bits = int(ap.GetParameterAsText(2))
    ght.gridsOfPolygon(input_path, bits, output_path)


if __name__ == '__main__':
    main()
