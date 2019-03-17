import sys
import os
import csv
import itertools

#part 1
total = 0
total_array = set()
inputfile = [int(x) for x in open("day1/input.csv").readlines()]
print(sum(inputfile))

# with open("day1/input.csv") as csvfile:
#     reader = csv.reader(csvfile, quoting=csv.QUOTE_NONNUMERIC) # change contents to floats
#     for row in reader: # each row is a list
#         total = total + row[0]

#part2
for x in itertools.cycle(inputfile):
    total = total + x
    if total in total_array :
        print(total)
        break
    total_array.add(total) 