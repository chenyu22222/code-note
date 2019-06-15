from pyspark import SparkContext

sc = SparkContext('local', 'test')

# UserID::MovieID::Rating::Timestamp
odd = sc.textFile('./ml-1m/ratings.dat')

# MovieID::Title::Genres
movie_file = sc.textFile('./ml-1m/movies.dat')

parts = odd.map(lambda row: row.split("::")).map(lambda l: (int(l[1]), int(l[2])))
movie_data = movie_file.map(lambda row: row.split("::")).map(lambda l: (int(l[0]), l[1])).collectAsMap()


def get_score(score):
    return score, 1


def to_avg(x, value):
    return x[0] + value, x[1] + 1


def get_avg(x, y):
    return x[0] + y[0], x[1] + y[1]


sum_count = parts.combineByKey(get_score, to_avg, get_avg)


def avg(row):
    return row[0], row[1][0] / row[1][1]


averageByKey = sum_count.map(avg)

movie_ratings = averageByKey.collectAsMap()
movie_ratings_sorted = sorted(movie_ratings.items(), key=lambda x: x[1], reverse=True)

result = []
for item in movie_ratings_sorted[:20]:
    data = (item[0], movie_data.get(item[0]), item[1])
    print(data)
    result.append(data)
