# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 11:56:28 2020

@author: WRShipway
"""

import pandas as pd

def DNA(database, sequence):
    '''
        Implement a program that identifies to whom a sequence of DNA belongs
        database - file containing Short Tandem Repeats (STRs)sequences 
          and corresponding names
        sequence - file containing the STR sequence
        
        Loop through STR's, ignoring name
        Loop through sequence, counting each repetition
        n :- integer to jump to next STR repeat, to ensure they are sequentially
          repeated

    Returns - name, or no match
    Results - Prints name, or "no match"

    '''
    STR, STR_matches = [], []
    i, n = 0, 0
    
    df_STR = pd.read_csv(database)
    df_sequence = pd.read_csv(sequence)
    sequence = df_sequence.columns[0]
    STR = df_STR.columns[1:]
    
    for i in range(len(STR)):
        j, STR_count_max = 0, 0
    
        while j < len(sequence):
            j = j + n # skip the while STR repeats
            STR_count, n = 0, 0
    
            while sequence[j + n:j + len(STR[i]) + n] == STR[i]:
                STR_count += 1
                n = STR_count * len(STR[i]) 
          
                if STR_count > STR_count_max:
                    STR_count_max = STR_count
            j += 1
            
        STR_matches.append(STR_count_max)
    
    ''' convert STR from dataframe to list, then remove names in list of lists '''
    STR_repeats = df_STR.values.tolist() # number of a persons STR repeats ''' 
    for _ in STR_repeats:
        _.pop(0)
    
    ''' print name and exit if a match is found '''
    for i in range(len(STR_repeats)):
        if STR_repeats[i] == STR_matches:
            #sys.exit()
            return df_STR.values[i][0]
    return("No match")