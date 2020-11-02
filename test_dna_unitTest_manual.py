# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 22:19:16 2020

@author: WRShipway
"""
import copy
import pandas as pd
import sys

'''
3. make a test script for each database/sequence input files
'''

STR, STR_matches = [], []
i, n = 0, 0
database = 'databases/small.csv'
sequence = 'sequences/4.txt'
#df_STR = pd.read_csv(database)
df_sequence = pd.read_csv(sequence)

df_STR = [['name', 'BB', 'AATG', 'TATC'],
          ['Alice', 2, 8, 3],
          ['Bob', 4, 1, 5],
          ['Charlie', 3, 2, 5],
          ['testName', 3, 0, 0]]

#sequence = df_sequence.columns[0]
sequence = "ABCDBBBBBBABCD"
STR = df_STR[0][1:]

for i in range(len(STR)):
    j, STR_count_max = 0, 0

    while j < len(sequence):
        j = j + n # skip the while STR repeats
        print ("j = %s, n = %s char = %s" % (j, n, sequence[j]))
        STR_count, n = 0, 0

        while sequence[j + n:j + len(STR[i]) + n] == STR[i]:
            print("j=%s, STR_count=%s, n=%s, STR=%s, STR max = %s, next char=%s" % 
                 (j, STR_count, n, sequence[j + n:j + len(STR[i]) + n], 
                  STR_count_max, sequence[j + n:j + len(STR[i]) + n+10]))
           
            STR_count += 1
            n = STR_count * len(STR[i])
            
            if STR_count > STR_count_max:
                STR_count_max = STR_count
                print("STR max = %s" % STR_count_max)
        j += 1
        
    # list the max STR repeats for each STR given
    STR_matches.append(STR_count_max)

# convert STR from dataframe to list, then remove names in list of lists
STR_repeats = copy.deepcopy(df_STR) # number of a persons STR repeats
for _ in STR_repeats:
    _.pop(0)

print('\n')
print(STR_repeats)
print(STR_matches)

# print name and exit if a match is found
for i in range(len(STR_repeats)):
    if STR_repeats[i] == STR_matches:
        print(df_STR[i][0])
        sys.exit()
print("No match")
