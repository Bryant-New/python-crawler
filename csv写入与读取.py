# coding=gbk
# ����csvģ�飬Python�Դ�������Ҫ�Լ�����д��,�ﺬopen������csvģ��ٷ��ĵ����ӣ�
# https://yiyibooks.cn/xx/python_352/library/csv.html#module-csv
import csv

# ����csv�ļ�������open()����������������ļ�����test.csv,д��ģʽ-
# ��w��-�Ը���ԭ������ʽд������ӵ����ݡ�newline=''-��β������-���Ա���csv�ļ������������оࣨ�����ܱ������������֮����ֿհ��У���encoding='utf-8'-�����ʽΪ����롣
# ��һ���ɶ�д��test.csv�ļ������������ݴ浽csv_file������
csv_file = open('test.csv', 'w', newline='', encoding='utf-8')
# ʹ��csv.writer()��������һ��writer���󣬽������ݵ�д��
writer = csv.writer(csv_file)
# ����writer�����writerow������csv�ļ���д���µ����ݣ�writerow������Ҫ�����б����
writer.writerow(['��Ӱ', '��������'])
writer.writerow(['���ӻ�����', '8.0'])
writer.writerow(['����������', '8.1'])
# д���ļ��󣬹ر��ļ�
csv_file.close()
# ��ȡcsv�ļ�������
import csv
# ��open()�򿪡�test.csv���ļ���'r'��read��ȡģʽ��newline=''�Ǳ�����������оࡣencoding='utf-8'�ܱ���������⵼�µı�������롣
csv_file = open('test.csv', 'r', newline='', encoding='utf-8')
# ʹ��csv.reader������ȡcsv_file����������һ��reader�����������csv_file�����ж�ȡ������
reader = csv.reader(csv_file)
# ��forѭ������reader����ӡrow����ȡ����test.csv��������
for row in reader:
    print(row)
csv_file.close()