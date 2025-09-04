import numpy as np
import pandas as pd
import json
myData=np.arange(0,1000000)
# print(myData)
# myFrame=pd.DataFrame(data=myData.reshape(1000,1000))
# print(myFrame)
# top 10 highest paid salary
# we need to first change combination
# myfile=("sample.json","w")
# we dont need import to csx
# myfile=("sample.csv","w")
myfile=("sample.xlsx","w")
myFrame=pd.DataFrame(data=myData.reshape(100000,10))
myFrame.to_excel("sample.xlsx")
# myFrame.to_csv("sample.csv")
# myFrame.to_json("sample.json")
print(myFrame.tail(1))
print(myFrame.loc[[2,]])
# # this prints the third row
# # loc will return the row index value
# # iloc will return the data in combintion of row and column 
print(myFrame.iloc[2:6,0:2]) # first is row and second one is column 
print(myFrame.iloc[2:5,7:10])
print(myFrame.iloc[8:10,4:6])
#write your data from dataframe to json file
#read data from json
# myjson=pd.read_json("sample.json")
# print(myjson)
# # read data from csv
# mycsv=pd.read_csv("sample.csv")
# print(mycsv)
# read data from excel
myexcel=pd.read_excel("sample.xlsx")
print(myexcel)