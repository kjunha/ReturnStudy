import numpy as np
import pandas as pd
f = open("data.csv", "r")
satisfaction = []
recommend = []
likereturn = []
lp = f.readlines()
print(len(lp))
for i in range(1, len(lp)):
    line = lp[i]
    dat = line.split(',')
    if len(dat) > 100:
            if dat[4] != '':
                    satisfaction.append(int(dat[4]))
            if dat[5] != '':
                    recommend.append(int(dat[5]))
            if dat[6] != '':
                    likereturn.append(int(dat[6]))

print("##### Satisfaction #####")
print(pd.Series(satisfaction).describe())
print("##### Recommendation #####")
print(pd.Series(recommend).describe())
print("##### Likelyhood to Return #####")
print(pd.Series(likereturn).describe())

df = pd.DataFrame({'sat': satisfaction, 'rec': recommend, 'ltr': likereturn})
print("##### Pearson Correlation #####")
print(df.corr('pearson'))

