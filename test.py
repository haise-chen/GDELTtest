import csv
import pandas as pd

# 定义要读取的CSV文件列表和要读取的列

'''
file_list = ['./201412/20141201.export.CSV', './201412/20141202.export.CSV', './201412/20141203.export.CSV',
             './201412/20141204.export.CSV', './201412/20141205.export.CSV', './201412/20141206.export.CSV',
             './201412/20141207.export.CSV', './201412/20141208.export.CSV', './201412/20141209.export.CSV',
             './201412/20141210.export.CSV', './201412/20141211.export.CSV', './201412/20141212.export.CSV',
             './201412/20141213.export.CSV', './201412/20141214.export.CSV', './201412/20141215.export.CSV',
             './201412/20141216.export.CSV', './201412/20141217.export.CSV', './201412/20141218.export.CSV',
             './201412/20141219.export.CSV','./201412/20141220.export.CSV', './201412/20141221.export.CSV',
             './201412/20141222.export.CSV', './201412/20141223.export.CSV', './201412/20141224.export.CSV',
             './201412/20141226.export.CSV', './201412/20141227.export.CSV', './201412/20141225.export.CSV',
             './201412/20141228.export.CSV', './201412/20141229.export.CSV', './201412/20141230.export.CSV',
             './201412/20141231.export.CSV',]
'''
file_list = ['./201401result.csv', './201402result.csv', './201403result.csv',
             './201404result.csv', './201405result.csv', './201406result.csv',
             './201407result.csv', './201408result.csv', './201409result.csv',
             './201410result.csv', './201411result.csv', './201412result.csv',]
#
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
        ls.append(line.split(","))  # 以\t为分隔符
    for line in ls:
        country = line[0]
        M = int(line[1])
        N = int(line[2])
        NMT = int(line[3])
        MMT = int(line[4])
        ABS = float(line[5])
        if not M_dict.get(country):
            M_dict[country] = M
        if not N_dict.get(country):
            N_dict[country] = N
        if not NMT_dict.get(country):
            NMT_dict[country] = NMT
        if not MMT_dict.get(country):
            MMT_dict[country] = MMT
        if not ABS_dict.get(country):
            ABS_dict[country] = ABS
'''
    for line in ls:
        country = line[51]
        mytype = line[29]
        if line[30]:
            score = abs(float(line[30]))
        else:
            score = 0
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

'''




for k, v in N_dict.items():
    # 该country总num
    if not a_dict.get(k):
        a_dict[k] = 0
    if v:
        a_dict[k] = float(ABS_dict[k] / v)
    else:
        a_dict[k] = 0

for k, v in N_dict.items():
    # 该country总num
    if not b_dict.get(k):
        b_dict[k] = 0
    if MMT_dict[k]:
        b_dict[k] = float(NMT_dict[k] / MMT_dict[k])
    else:
        b_dict[k]=0

for k, v in M_dict.items():
    # 该country总num
    if not c_dict.get(k):
        c_dict[k] = 0
    if a_dict.get(k) and b_dict.get(k):
        c_dict[k] = a_dict[k]*b_dict[k]

for key, value in c_dict.items():
    print(key, value)

content = []
for k, v in c_dict.items():
    content.append([k, str(v)])
with open("./2014result.csv", 'w', newline='') as f:
    # 写入文件
    for line in content:
        try:
            # 以逗号分隔一行的每个元素，后接一个换行符
            f.write(",".join(line) + "\n")

        except Exception as e:
            print(e)

'''
content = []
for k, v in M_dict.items():
    if not N_dict.get(k):
        N_dict[k] = 0
        NMT_dict[k] = 0
        ABS_dict[k] = 0
    content.append([k, str(v), str(N_dict[k]), str(NMT_dict[k]), str(MMT_dict[k]), str(ABS_dict[k])])
with open("./201412result.csv", 'w', newline='') as f:
    # 写入文件
    for line in content:
        try:
            # 以逗号分隔一行的每个元素，后接一个换行符
            f.write(",".join(line) + "\n")

        except Exception as e:
            print(e)
        '''