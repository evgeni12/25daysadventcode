import sys
import os
import csv
import itertools
from collections import Counter

#Part1
letters2 = 0
letters3 = 0
inputfile = open("day2/input.csv").read().splitlines()
# for x in inputfile:
#     letters2Bool = False
#     letters3Bool = False
#     counter = Counter(x)
#     for x in counter :
#         if counter[x] == 2 and letters2Bool == False:
#             letters2 +=1
#             letters2Bool = True
#         elif counter[x] == 3 and letters3Bool == False:
#             letters3 +=1
#             letters3Bool = True

# print(letters2 * letters3)


#part2
word1 = None
word2 = None
count = None

def dif(a, b):
    return [i for i in range(len(a)) if a[i] != b[i]]

for x in inputfile:
    for y in inputfile:
        if word1 == None and word2 == None and x != y:
            word1 = x
            word2 = y
            count = dif(x, y)
        elif x != y:
            temp_count = dif(x, y)
            if len(temp_count) < len(count):
                word1 = x
                word2 = y
                count = temp_count
print(word1)
print(word2)
print(count)

final_word = word1[:count[0]] + word1[count[0]+1:]
print(final_word)
