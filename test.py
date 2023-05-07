import csv
import pandas as pd

# 定义要读取的CSV文件列表和要读取的列
file_list = ['./201001.csv', './201002.csv', './201003.csv',
             './201004.csv', './201005.csv', './201006.csv',
             './201007.csv', './201008.csv', './201009.csv',
             './201010.csv', './201011.csv', './201012.csv']
country_index = 51
type_index = 29  # 例如，读取第一列的值
score_index = 30  # 例如，读取第二列的值
time_index = 31  # 例如，读取第二列的值
# 初始化字典
M_dict = {}
N_dict = {}
NMT_dict = {}
MMT_dict = {}
ABS_dict = {}
a_dict = {}
b_dict = {}
c_dict = {}
i = 0
# 循环遍历文件列表并逐个读取CSV文件
for file_name in file_list:

    fo = open(file_name, 'r', newline='', encoding='utf-8-sig')  # 打开csv文件
    ls = []
    for line in fo:
        line = line.replace("\n", "").replace("\r", "")  # 去掉将换行符
        # columns = [x for x in line.split("\t") if x]
        ls.append(line.split("\t"))  # 以\t为分隔符
    for line in ls:
        country = line[51]
        mytype = line[29]
        score = abs(float(line[30]))
        times = int(line[31])
        if country:
            if not M_dict.get(country):
                M_dict[country] = 0
            if not MMT_dict.get(country):
                MMT_dict[country] = 0


            M_dict[country] = M_dict[country] + 1

            MMT_dict[country] = MMT_dict[country] + times

            if mytype in ["3", "4"]:
                if not N_dict.get(country):
                    N_dict[country] = 0
                if not ABS_dict.get(country):
                    ABS_dict[country] = 0
                if not NMT_dict.get(country):
                    NMT_dict[country] = 0
                # 计算国家冲突新闻总数N
                N_dict[country] = N_dict[country] + 1
                # 计算国家冲突新闻分值
                ABS_dict[country] = ABS_dict[country] + score
                # 计算国家冲突新闻提及次数
                NMT_dict[country] = NMT_dict[country] + times

    i += 1
    print(i)


for k, v in N_dict.items():
    # 该country总num
    if not a_dict.get(k):
        a_dict[k] = 0
    a_dict[k] = float(ABS_dict[k] / v)

for k, v in N_dict.items():
    # 该country总num
    if not b_dict.get(k):
        b_dict[k] = 0
    b_dict[k] = float(NMT_dict[k] / MMT_dict[k])

for k, v in M_dict.items():
    # 该country总num
    if not c_dict.get(k):
        c_dict[k] = 0
    if a_dict.get(k) and b_dict.get(k):
        c_dict[k] = a_dict[k]*b_dict[k]
''''
for key, value in c_dict.items():
    print(key, value)
'''

content = []
for k, v in c_dict.items():
    content.append([k, str(v)])
with open("./2010result.csv", 'w', newline='') as f:
    # 写入文件
    for line in content:
        try:
            # 以逗号分隔一行的每个元素，后接一个换行符
            f.write(",".join(line) + "\n")

        except Exception as e:
            print(e)



