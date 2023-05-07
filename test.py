'''
该代码适用于新闻年份文件
即到2005年为止
'''


import os
from functools import reduce


class Analyze(object):
    def __init__(self, csv_path):
        self.csv_path = csv_path
        self.csv_content = self.csv2json()
        self.countrya = {}
        self.countryb = {}
        self.countryc = {}
        self.country = {}

    def csv2json(self):
        fo = open(self.csv_path, 'r', newline='', encoding='utf-8-sig')  # 打开csv文件
        ls = []
        for line in fo:
            line = line.replace("\n", "").replace("\r", "")  # 去掉将换行符
            # columns = [x for x in line.split("\t") if x]
            ls.append(line.split("\t"))  # 以\t为分隔符
        return ls
        # print(ls[9])
        # print(len(ls[9]), ls[9][29:32], ls[9][44])

    def calc_q1(self):
        country_34_num = {}
        country_num = {}
        country_31_num = {}
        for line in self.csv_content:
            country = line[51]
            c30 = line[29]
            c31 = line[30]
            if country:
                if not self.country.get(country):
                    self.country[country] = 0
                self.country[country] = self.country[country] + 1

                if c30 in ["3", "4"]:
                    if not country_34_num.get(country):
                        country_34_num[country] = 0
                    country_34_num[country] = country_34_num[country] + 1
                '''
                if c31:
                    if not country_31_num.get(country):
                        country_31_num[country] = 0
                    country_31_num[country] = country_34_num[country] + abs(int(c31))
                '''
        for k, v in country_34_num.items():
            '''
            # 该country总num
            print("country {} c30 3/4 num: {}, summary num: {}".format(k, v, country_num[k]))
            '''
        return country_num, country_34_num

    def calc_q2(self):
        country_34_num = {}
        country_num = {}
        country_31_num = {}
        for line in self.csv_content:
            country = line[51]
            c30 = line[29]
            c31 = line[30]
            if country:
                if not country_num.get(country):
                    country_num[country] = 0
                country_num[country] = country_num[country] + 1

                if c30 in ["3", "4"]:
                    if not country_34_num.get(country):
                        country_34_num[country] = 0
                    country_34_num[country] = country_34_num[country] + 1
                    if c31:
                        if not country_31_num.get(country):
                            country_31_num[country] = 0
                        res = abs(float(c31))
                        country_31_num[country] = country_31_num[country] + res

        for k, v in country_34_num.items():
            # 该country总num
            if not self.countrya.get(k):
                self.countrya[k] = 0
            self.countrya[k] = float(country_31_num[k] / v)
            #print("country {} c30 3/4 num: {}, summary num: {}".format(k, v, self.a))
        return country_num, country_34_num

    def calc_q3(self):
        country_34_num = {}
        country_num = {}
        country_32_num = {}
        country_32_34_num = {}
        for line in self.csv_content:
            country = line[51]
            c30 = line[29]
            c32 = line[31]
            if country:
                if not country_num.get(country):
                    country_num[country] = 0
                country_num[country] = country_num[country] + 1

                if c32:
                    if not country_32_num.get(country):
                        country_32_num[country] = 0
                    res = int(c32)
                    country_32_num[country] = country_32_num[country] + res

                if c30 in ["3", "4"]:
                    if not country_34_num.get(country):
                        country_34_num[country] = 0
                    country_34_num[country] = country_34_num[country] + 1
                    if c32:
                        if not country_32_34_num.get(country):
                            country_32_34_num[country] = 0
                        res = int(c32)
                        country_32_34_num[country] = country_32_34_num[country] + res

        for k, v in country_32_34_num.items():
            # 该country总num
            if not self.countryb.get(k):
                self.countryb[k]=0
            self.countryb[k] = float(country_32_34_num[k] / country_32_num[k])
            #print("country {} c30 3/4 num: {}, summary num: {}".format(k, v, country_num[k]))
        return self

    def calc_q4(self):
        for k, v in self.countrya.items():
            # 该country总num
            if not self.countryc.get(k):
                self.countryc[k] = 0
            if self.countrya.get(k) and self.countryb.get(k):
                self.countryc[k] = self.countrya[k] * self.countryb[k]
            print("country {} c num: {},".format(k, self.countryc[k]))

    def calc(self):
        # res1 = self.calc_q1()

        self.calc_q1()
        self.calc_q2()
        self.calc_q3()
        self.calc_q4()
        content = []
        for k, v in self.countryc.items():
            content.append([k, str(v)])
        self.json2csv(content=content)

    @staticmethod
    def json2csv(content):
        """
        content参数是两层嵌套的list
        """
        with open("./1995result.csv", 'w', newline='') as f:
            # 写入文件
            for line in content:
                try:
                    # 以逗号分隔一行的每个元素，后接一个换行符
                    f.write(",".join(line) + "\n")

                except Exception as e:
                    print(e)


if __name__ == '__main__':
    a = Analyze(csv_path="./1995.csv")
    a.calc()
