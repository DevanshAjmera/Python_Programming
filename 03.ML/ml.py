# Mean :- Average of Dataset
import numpy as np

dataset = [70,90,65,60,80,60]
mean = np.mean(dataset)
print("Mean: ",mean)

median = np.median(dataset)
print("Median:",median)

from scipy import stats
mode = stats.mode(dataset)
print("Mode: ",mode)

#Standard Deviation is square root of variance...
SD = np.std(dataset)
print("Standard Deviation: ",SD)
variance = np.var(dataset)
print("Variance: ",variance)


max = np.max(dataset)
min = np.min(dataset)
print("Max: ",max)
print("Min: ",min)

#Data Distribution is a technique to arranging the data in order
#Normal Distribution 
uniformdata = np.random.uniform(1,10,500)
print("\n",uniformdata)

