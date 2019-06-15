from pyspark import SparkContext
import matplotlib.pyplot as plt

sc = SparkContext()

# MovieID::Title::Genres
movie_file = sc.textFile('./ml-1m/movies.dat')


movie = movie_file.map(lambda row: row.split("::"))\
    .flatMap(lambda row: [(c, {int(row[0])}) for c in row[2].split("|")])\
    .reduceByKey(lambda x, y: x | y)\
    .map(lambda row: (row[0], len(row[1])))


# print(movie.collect())


plt.barh(movie.map(lambda row: row[0]).collect(), movie.map(lambda row: row[1]).collect(), linewidth=2)
plt.show()