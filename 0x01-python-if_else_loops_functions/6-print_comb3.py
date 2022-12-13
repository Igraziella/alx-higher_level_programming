#!/usr/bin/python3
#Python program to print all the possible
#combinations
from  itertools import permutations
comb = permutations(range(10), 2)

for i in comb:
    print(i[0],i[1], end="")
