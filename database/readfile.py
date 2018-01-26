import pandas as pd
import numpy as np

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

