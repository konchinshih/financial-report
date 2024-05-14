import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

MARKET = '^TWII'
SOURCES = ['2607.TW', '2609.TW', '2610.TW']


def getApprox(source: str) -> pd.DataFrame:
    approx = pd.read_csv(f"{source}.approx.csv")
    
    approx['ReturnRate'] = approx['Close'].pct_change()

    return approx


marketApprox = getApprox(MARKET)

def getTest(source: str) -> pd.DataFrame:
    test = pd.read_csv(f"{source}.test.csv")

    test['ReturnRate'] = test['Close'].pct_change()

    return test

marketTest = getTest(MARKET)

def calcParams(approx: pd.DataFrame) -> (int, int):
    # R_t = alpha + beta * R_mt + epsilon

    marketMean = marketApprox['ReturnRate'].mean()
    approxMean = approx['ReturnRate'].mean()

    Sxy = ((marketApprox['ReturnRate'] - marketMean) \
        * (approx['ReturnRate'] - approxMean)).sum()

    Sxx = ((marketApprox['ReturnRate'] - marketMean) ** 2).sum()

    beta = Sxy / Sxx
    alpha = approxMean - beta * marketMean

    return (alpha, beta)


def calcAbnormal(test: pd.DataFrame, alpha: int, beta: int) -> None:
    # AR_t = R_t - alpha - beta * R_mt

    test['AbnormalReturnRate'] \
        = test['ReturnRate'] - alpha - beta * marketTest['ReturnRate']
    test['CumulativeAbnormalReturnRate'] \
        = test['AbnormalReturnRate'].cumsum()
    

AR = pd.DataFrame()
AR['Date'] = marketTest['Date']

CAR = pd.DataFrame()
CAR['Date'] = marketTest['Date']

for source in SOURCES:

    approx = getApprox(source)
    alpha, beta = calcParams(approx)
    
    test = getTest(source)
    calcAbnormal(test, alpha, beta)

    AR[source] = test['AbnormalReturnRate']
    CAR[source] = test['CumulativeAbnormalReturnRate']

AR['average'] = sum(AR[source] for source in SOURCES) / len(SOURCES)
CAR['average'] = sum(CAR[source] for source in SOURCES) / len(SOURCES)

sns.lineplot(data=AR, x='Date', y='average')
plt.title('Average Abnormal Return Rate')
plt.show(); 

sns.lineplot(data=CAR, x='Date', y='average')
plt.title('Average Cumulative Abnormal Return Rate')
plt.show()
