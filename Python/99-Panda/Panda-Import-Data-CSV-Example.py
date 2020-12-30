# -*- coding: utf-8 -*-
"""
Created on Wed Dec 30 14:01:26 2020

@author: SethHarden
"""

# Import pandas package  
import pandas as pd  
    
# making data frame  
data = pd.read_csv("https://media.geeksforgeeks.org/wp-content/uploads/nba.csv")  
    
# calling head() method   
# storing in new variable  
data_top = data.head()  
    
# display  
data_top 

for col in data.columns: 
    print(col) 