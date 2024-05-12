import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

approx = pd.read_csv("2607.TW.approx.csv")

approx['ReturnRate'] = approx['Close'].pct_change()

#sns.lineplot(data=approx, x='Date', y='ReturnRate')
#plt.savefig("test"); plt.show()

approxMean = approx['ReturnRate'].mean()
print(approxMean)

test = pd.read_csv("2607.TW.test.csv")

test['ReturnRate'] = test['Close'].pct_change()
test['AbnormalReturnRate'] = test['ReturnRate'] - approxMean

sns.lineplot(data=test, x='Date', y='AbnormalReturnRate')
plt.savefig("test"); plt.show()

exit()
