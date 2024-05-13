import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
import statistics as st
from scipy import stats
from statsmodels.stats.weightstats import ztest
import numpy as np

approx = pd.read_csv("2607.TW.approx.csv")
test = pd.read_csv("2607.TW.test.csv")

ind = data.loc[data['isOffice'] == 0]
office = data.loc[data['isOffice'] == 1]


#   Question 1
test11 = ztest(
    ind['fan'],
    office['fan'],
    alternative='smaller'
)

test12 = ztest(
    ind['fan'],
    office['fan'],
    alternative='larger'
)

print(test11)
print(test12)

#   Question 2
ind = ind.sort_values(
    by=['viewRate']
).iloc[
    len(ind.index)*5//100:len(ind.index)*95//100
]
office = office.sort_values(
    by=['viewRate']
).iloc[
    len(office.index)*5//100:len(office.index)*95//100
]

test21 = ztest(
    ind['viewRate'],
    office['viewRate'],
    alternative='smaller'
)

test22 = ztest(
    ind['viewRate'],
    office['viewRate'],
    alternative='larger'
)

print(test21)
print(test22)


#   Question 3
firstHalf = data.iloc[lambda x: x.index < len(data.index)//2]
firstHalf = firstHalf.sort_values(
    by=['viewRate']
).iloc[
    len(firstHalf.index)*5//100:len(firstHalf.index)*95//100
]
secondHalf = data.iloc[lambda x: x.index >= len(data.index)//2]
secondHalf = secondHalf.sort_values(
    by=['viewRate']
).iloc[
    len(secondHalf.index)*5//100:len(secondHalf.index)*95//100
]

test31 = ztest(
    firstHalf['viewRate'],
    secondHalf['viewRate'],
    alternative='smaller'
)

test32 = ztest(
    firstHalf['viewRate'],
    secondHalf['viewRate'],
    alternative='larger'
)

print(test31)
print(test32)
