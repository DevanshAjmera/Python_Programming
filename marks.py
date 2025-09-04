import numpy as np
import matplotlib.pyplot as plt
from scipy import stats as st
from sklearn.metrics import r2_score
#*finding future data : prediction: regression:
# linear regtression: it find the relation in between variable as data set
# y=mx+c
marks = [20,25,30,22,40,50,45,34]
year= [2016,2017,2018,2019,2020,2021,2022,2023]
slope,intercept,r,p,std_err = st.linregress(marks,year)
print("Slope",slope,"Intercept",intercept,"R",r,"P",p,"Std_err",std_err)

def futuremarks(year):
    return slope*year+intercept
print("futuremarks",futuremarks(2024))
plt.scatter(marks, year, color='blue')
plt.xlabel('year')
plt.ylabel('marks')
plt.title('year vs. marks Scatter Plot')
plt.show()

