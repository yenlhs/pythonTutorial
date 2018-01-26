import pandas as pd
import numpy as np
import matplotlib.pyplot as mp

#change this variable to adjust the number of rows to display. 
#Write None if you wish to display all rows
numrows = 3

#path to csv file 
filepath = '/Users/Adrian/Documents/pythonTutorial/database/'
#name of csv file
csvfile = 'test.csv'

#read csv file and assign to object df
df = pd.read_csv(filepath+csvfile,index_col=0,encoding='utf-8',nrows=numrows)

#print dataframe
print(df)

mp.plot([1,2,3,4],[1,2,5,12])
mp.xlabel('x numbers')
mp.ylabel('some numbers')
mp.show()





