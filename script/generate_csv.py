import os
import csv

path_data = '../data'
csvfile = open('face.csv', 'w')  # 打开方式还可以使用file对象
files = os.listdir(path_data)  # 得到文件夹下所有文件的名称
# os.walk()返回一个三元素的tuple：当前路径、子文件夹名称、文件列表。
for root, dirs, files in os.walk(path_data):
    for filename in files:
        print(root + '/' + filename + ';' + '0')
        writer = csv.writer(csvfile)
        writer.writerow([root + '/' + filename + ';' + '0'])
csvfile.close()
