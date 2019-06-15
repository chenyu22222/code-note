from pyspark import SparkContext
from matplotlib import pyplot as plt


sc = SparkContext()

# UserID::Gender::Age::Occupation::Zip-code
movie_file = sc.textFile('./ml-1m/users.dat')


def sex_num(row):
    sexs = list(row[1])
    sex = set(sexs)
    return [(row[0] + s, sexs.count(s)) for s in sex]


users = movie_file.map(lambda row: row.split("::"))\
    .map(lambda row: (row[3], row[1]))\
    .groupByKey().flatMap(sex_num).collect()


labels = []
sizes = []
for key, value in users:
    if key[:-1] in ("1", "6", "16"):
        labels.append(key)
        sizes.append(value)


plt.figure(figsize=(6, 6))  # 调节图形大小

patches, text1, text2 = plt.pie(sizes,
                                labels=labels,
                                autopct='%0.2f%%',  # 数值保留固定小数位
                                shadow=False,  # 无阴影设置
                                startangle=90,  # 逆时针起始角度设置
                                pctdistance=0.6)  # 数值距圆心半径倍数距离

# patches饼图的返回值，texts1饼图外label的文本，texts2饼图内部的文本
# x，y轴刻度设置一致，保证饼图为圆形
plt.axis('equal')
plt.show()
