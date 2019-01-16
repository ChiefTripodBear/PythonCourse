import numpy as np
from scipy import stats
from scipy.stats.stats import pearsonr


#central tendencies
dataset = np.array([3,1,4,1,1,7,10,15,2,5,12,8])
mean = np.mean(dataset)
median = np.median(dataset)
mode = stats.mode(dataset)

print(f'the mean is: {mean}.')
print(f'the median is: {median}.')
print(f'the mode is: {mode}.')

#covariance
x = np.random.normal(size=2)
y = np.random.normal(size=2)
z = np.vstack((x, y))

c = np.cov(z. T) #the T denotes that each ROW is a variable, and the columns are observations.
                # a F would mean that each COLUMN is a variable, and the rows are observations.
print(x)
print(y)
print(c)

#r2 statistic
a = [1,4,6]
b = [1,2,3]
corr = pearsonr(a,b)
print(f'correlation of {a} and {b} is: {corr}')

corr = pearsonr(x, y)
print (f'correlation of {x} and {y} is: {corr}')


