import pandas as pd
    
# making data frame from csv file 
data = pd.read_csv("nba.csv")   
    
# Integer slicing 
print("Slicing only rows(till index 4):") 
x1 = data.iloc[:4, ]
#x1 = data.ix[:4, ] 
print(x1, "\n") 
   
print("Slicing rows and columns(rows=4, col 1-4, excluding 4):") 
#x2 = data.ix[:4, 1:4] 
x2 = data.iloc[:4, 1:4]
print(x2, "\n") 



s = pd.Series(list('abca'))
print(s)
s1 = ['a', 'b', 'a', 'a']
print(s1)
print(pd.get_dummies(s1))