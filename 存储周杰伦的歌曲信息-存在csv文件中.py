#  coding: gbk
# Python�������-��ȡ����-��������-��ȡ����-�洢����
import requests
import openpyxl

# csv�ļ�д�룺1.�����ļ�-����open����2.��������-����writer����3.д������-writerow����4.�ر��ļ�
# import csv
# csv_file = open('demo.csv','w',newline='')
# writer = csv.writer(csv_file)
# writer.writerow(['��Ӱ','��������'])
# csv_file.close()

# csv�ļ���ȡ��1.���ļ�-����open����2.��������-����reader����3.��ȡ����-����reader����4.��ӡ����
# import csv
# csv_file = open('demo.csv','r',newline='')
# reader=csv.reader(csv_file)
# for row in reader:
#     print(row)

# Excel�ļ�д�룺1.����������-openpyxl.Workbook()2.��ȡ������-workbook�е�active����3.������Ԫ��-append4.���湤����-save
# import openpyxl
# wb = openpyxl.Workbook()
# sheet = wb.active
# sheet.title ='new title'
# sheet['A1'] = '��������'
# rows = [['�����ӳ�','������','֩����','����'],['��','����','����', '����','����']]
# for i in rows:
#     sheet.append(i)
# print(rows)
# wb.save('Marvel.xlsx')

# Excel�ļ���ȡ��1.����������-openpyxl.Workbook()2.��ȡ������-workbook����ļ�3.��ȡ��Ԫ��-������Ԫ��value����4.��ӡ��Ԫ��
# import openpyxl
# wb = openpyxl.load_workbook('Marvel.xlsx')
# sheet = wb['new title']
# sheetname = wb.sheetnames
# print(sheetname)
# A1_value = sheet['A1'].value
# print(A1_value)
