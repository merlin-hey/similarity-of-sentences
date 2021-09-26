import re
import numpy
import scipy.spatial.distance
all_words = []
unique_words = []
f = open("sentences.txt", 'r')
for line in f:
    line = line.lower()
    words_in_one_sentence = re.split(r"[^a-z]", line)
    all_words.append([x for x in words_in_one_sentence if x != ''])
print(all_words)
for sentence in all_words:
    for item in sentence:
        unique_words.append(item)
unique_words = set(unique_words)
dict_of_unique_words = {x: y for x, y in zip(range(len(unique_words)), tuple(unique_words))}
print(dict_of_unique_words)
n = len(all_words)
d = len(unique_words)
matrix = numpy.zeros((n, d))
for string in range(n):
    for column in range(d):
        matrix[string][column] = all_words[string].count(dict_of_unique_words[column])
print(matrix)
print(numpy.shape(matrix))
dist = []
for string in matrix:
    dist.append(scipy.spatial.distance.cosine(matrix[0], string))
print(dist.index(min(dist)))
del dist[0]
min_1 = dist.index(min(dist))
print(min_1)
del dist[5]
min_2 = dist.index(min(dist))
print(min_2)
