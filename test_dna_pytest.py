# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 11:56:28 2020

@author: WRShipway
"""
import pandas as pd
from dna import DNA

if __name__ == "__main__":
    database_list = ["small" if i < 4 else "large" for i in range(20)] 
    
    assert_list = [
                  "Bob",
                  "No match",
                  "No match",
                  "Alice",
                  "Lavender",
                  "Luna",
                  "Ron",
                  "Ginny",
                  "Draco",
                  "Albus",
                  "HermioneTest",
                  "Lily",
                  "No match",
                  "Severus",
                  "Sirius",
                  "No match",
                  "Harry",
                  "No match",
                  "Fred",
                  "No match"]

    for i in range(len(database_list)):
        database = 'databases/{}.csv' .format(database_list[i])
        sequence = 'sequences/{}.txt' .format(i+1)
        df_STR = pd.read_csv(database)
        df_sequence = pd.read_csv(sequence)
        result = DNA(database, sequence)
        
        assert result == assert_list[i],  \
        "--error in test {}--\nYour program should output '{}'" \
        .format((i+1), assert_list[i])
        
        if DNA(database, sequence) != assert_list[i]:
            pass
            #print("--error in test {}--". format(i+1))
