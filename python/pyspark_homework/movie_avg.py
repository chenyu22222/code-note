from pyspark import SparkContext
import numpy as np

sc = SparkContext('local', 'test')

# UserID::MovieID::Rating::Timestamp
odd = sc.textFile('./ml-1m/ratings.dat')

# MovieID::Title::Genres
movie_file = sc.textFile('./ml-1m/movies.dat')

parts = odd.map(lambda row: row.split("::")).map(lambda l: (int(l[1]), int(l[2])))
movie_data = movie_file.map(lambda row: row.split("::")).map(lambda l: (int(l[0]), l[1][:-6].strip()))


def get_score(score):
    return score, 1


def to_avg(x, value):
    return x[0] + value, x[1] + 1


def get_avg(x, y):
    return x[0] + y[0], x[1] + y[1]


def avg(row):
    return row[0], row[1][0] / row[1][1]


movie_ratings = parts.combineByKey(get_score, to_avg, get_avg).map(avg)


def standard_deviation(row):
    return row[0], np.std(row[1][1], ddof=1)


std_count = parts.combineByKey(lambda s: (s, [s]),
                               lambda x, v: (x[0]+v, x[1]+[v]),
                               lambda x, y: (x[0]+y[0], x[1]+y[1])
                               )

movie_std = std_count.map(standard_deviation)

# (movieName, 平均值, 标准差)
result = movie_data.join(movie_ratings).join(movie_std).map(lambda row: (row[1][0][0], row[1][0][1], row[1][1])).collect()


for item in result:
    print(item)
