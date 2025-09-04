"""Find the future data :- Prediction :- Regression
Linear Regression:- it find the relation in between variable or dataset scatters  y=mx+c
                    has a limitation to predict the future value if r is nearby 0
                    when we use linear regression if r is nearby 1 
Polynomial regerssion :- is used when linear regression doesnt give the best result                                            
"""
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score
from scipy import stats as st

"""age = [20, 25, 30, 22, 40, 50, 45]
salary = [20000, 25000, 30000, 22000, 40000, 50000, 45000]
slope, intercept, r, p, std_err = st.linregress(age,salary)
print("Slope",slope,"Intercept",intercept,"R",r,"P",p,"Std_err",std_err)
def futureSalary(age):
    return slope *age + intercept
print("FutureSalary",futureSalary(35))
plt.scatter(age, salary, color='blue')
plt.xlabel('Age')
plt.ylabel('Salary')
plt.title('Age vs. Salary Scatter Plot')
plt.show()
"""


# prediction
"""age=[20,25,45,30,50,60]
salary=[40000,15000,20000,25000,22000,45000]
futureSalary=np.poly1d(np.polyfit(age,salary,3))
print(r2_score,salary,futureSalary(35))
print(futureSalary(55))
print(futureSalary(18))
# find r2_score 
print(r2_score(salary(futureSalary(age))))
"""

"""
#Find the amazon, flipkart, swiggy, zomato, goibibo, makemytrip, oyo
#Swiggy revenue data of last 5 years...
year = [2019,2020,2021,2022,2023]
revenue = [3500,4500,6000,8000,10000]
slope,intercept,r,p,std_err = st.linregress(year,revenue)
print("Slope",slope,"Intercept",intercept,"R",r,"P",p,"Std_err",std_err)
def futurerevenue(year):
    return slope*year+intercept
print("future revenue",futurerevenue(2024))
plt.scatter(year, revenue, color='blue')
plt.xlabel('year')
plt.ylabel('Revenue')
plt.title('year vs. Sales Scatter Plot')
plt.show()
"""


# Model in machine learning for supervised and unsupervised data
# Model in unsupervised dataset 
# K mean model :- Is the unsupervised machine learning data technique for making clustering. 
#               This model will divide the data points into k cluster for minimizing the variance in dataset
from sklearn.cluster import KMeans
age = [60,50,40,42,55]
salary = [50000,40000,35000,39000,45000] 
# plt.scatter(age,salary, color='blue')
# plt.xlabel('Age')
# plt.ylabel('Salary')
# plt.title('Scatter Graph')
# plt.show()

data = list(zip(age,salary))
blank_array = []
for mydata in range(1,6):
    kmean = KMeans(n_clusters=mydata)
    kmean.fit(data)
    blank_array.append(kmean.inertia_)
plt.plot(range(1,6), blank_array, marker='o')
plt.xlabel('Number of clusters')
plt.ylabel('Inertia')
plt.show()