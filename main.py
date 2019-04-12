import numpy as np
import pandas as pd
f = open("data_cc.csv", "r", encoding = "utf-8")
satisfaction = []
recommend = []
likereturn = []
cnt = 0
lp = f.readlines()
print(len(lp))
for i in range(1, len(lp)):
    line = lp[i]
    dat = line.split(',')
    if len(dat) > 100:
            if dat[4] != '' and dat[5] != '' and dat[6] != '':
                    satisfaction.append(int(dat[4]))
                    recommend.append(int(dat[5]))
                    likereturn.append(int(dat[6]))
                    if int(dat[6]) < 7 and int(dat[5]) >= 9:
                            cnt = cnt + 1

print (cnt)
print("##### Satisfaction #####")
print(pd.Series(satisfaction).describe())
print("##### Recommendation #####")
print(pd.Series(recommend).describe())
print("##### Likelyhood to Return #####")
print(pd.Series(likereturn).describe())

df = pd.DataFrame({'sat': satisfaction, 'rec': recommend, 'ltr': likereturn})
print("##### Pearson Correlation #####")
print(df.corr('pearson'))

