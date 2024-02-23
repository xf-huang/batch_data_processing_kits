# -*- coding: utf-8 -*-
import arcpy
# �滻Ϊ��Ҫ����ֶε�gdb�ļ�·��
arcpy.env.workspace = r"C:\Users\admin\Desktop\�½��ļ��� (4)\���кϲ�.gdb"
# ��ȡgdb������Ҫ����
feature_classes = arcpy.ListFeatureClasses()
# �滻Ϊ��Ҫ��ӵ��ֶ���Ϣ���б���һ��Ԫ��Ϊһ���ֶΣ�Ԫ���е�һ��Ԫ�����ֶ������ڶ���Ԫ�����ֶ����ͣ�������Ԫ�����ֶα��������ĸ�Ԫ�����ֶγ���
fields_to_add = [
	("OCEAN_DATA_IDENTIFICATION_CODE", "TEXT", "�������ݱ�ʶ��", 27),
	("ADMINISTRATIVE_DIVISION", "TEXT", "��������", 64),
	("ADMINISTRATIVE_DIVISION_CODE", "TEXT", "������������", 12),
	("GEO_AREA", "DOUBLE", "���������ƽ���ף�", None)
	]
# ѭ��Ϊgdb��ÿ��Ҫ��������ֶ�
for fc in feature_classes:
	for field in fields_to_add:
		name, data_type, alias, length = field
		arcpy.AddField_management(in_table=fc, field_name=name, field_type=data_type, field_length=length, field_alias=alias)
print("����ֶγɹ�")
