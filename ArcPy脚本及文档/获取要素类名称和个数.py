# -*- coding: gbk -*-

import arcpy

gdb = r'D:\download\�۲�վ��ʸ����.gdb'
arcpy.env.workspace = gdb

featureclasses = arcpy.ListFeatureClasses()

for fc in featureclasses:
    name = fc
    count = arcpy.GetCount_management(fc).getOutput(0)
    print(name + '(' + count + ')')
