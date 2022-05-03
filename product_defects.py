import scipy.stats as stats
import numpy as np

### Task Group 1 ###
## Task 1: 
#Create a variable called lam that represents the rate parameter of our distribution.
lam = 7

## Task 2:
# Calculate and print the probability of observing exactly lam defects on a given day.
print(stats.poisson.pmf(lam, lam))

## Task 3:
# Our boss said that having 4 or fewer defects on a given day is an exceptionally good day. You are curious about how often that might happen.
# Calculate and print the probability of having one of these days.
print(stats.poisson.cdf(4, lam))

## Task 4:
# On the other hand, our boss said that having more than 9 defects on any given day is considered a bad day.
# Calculate and print the probability of having one of these bad days.
print(1 - stats.poisson.cdf(9, lam))

### Task Group 2 ###
## Task 5:
year_defects = stats.poisson.rvs(lam, size = 365)

## Task 6:
print(year_defects[:20])

## Task 7:
print(lam * 365)

## Task 8:
print(np.sum(year_defects))

## Task 9:
print(np.mean(year_defects))

## Task 10:
print(max(year_defects))

## Task 11:
print(1 - stats.poisson.cdf(max(year_defects) -1, lam))

### Extra Bonus ###
# Task 12
print(stats.poisson.ppf(0.9, lam))

# Task 13
print(sum(year_defects > stats.poisson.ppf(0.9, lam))/len(year_defects))