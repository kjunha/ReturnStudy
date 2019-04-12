import numpy as np
import pandas as pd
import random

# Random Number Sequence
def writeRand50(arr):
    pool = len(arr)
    randset = []
    for i in range(pool):
        randset.append(i)

    rand50 = random.sample(randset, 50)
    print("Randomize Ready")
    f = open("comout.csv", "a", encoding="utf8")
    #Write r7hrc
    for x in range(len(rand50)):
        i = rand50[x]
        f.write(arr[i] + "\n")
    f.close()


f = open("data_com.csv", "r", encoding="utf8")
lp = f.readlines()
#Return Score 7, but recommanded 9, 10 (High) as r7hrc(High Recommendation)
r7hrc = []
#Return Score 7, but recommanded 7, 8 (Low) as r7lrc(Low Recommendation)
r7lrc = []

print(len(lp))
for i in range(1, len(lp)):
    line = lp[i]
    dat = line.split(',')
    if dat[5] != '' and dat[6] != '':
        if int(dat[6]) < 7 and int(dat[5]) >= 9:
            ln = "High Rec" + ","
            if dat[93] != '':
                ln = ln + dat[93] + ","
            else :
                ln = ln + ","
            if dat[94] != '':
                ln = ln + dat[94] + ","
            r7hrc.append(ln)
        elif int(dat[6]) < 7 and int(dat[5]) >= 7:
            ln = "Low Rec" + ","
            if dat[93] != '':
                ln = ln + dat[93] + ","
            else :
                ln = ln + ","
            if dat[94] != '':
                ln = ln + dat[94] + ","
            r7lrc.append(ln)

print("Search Finish.")

#open file and write all
print(len(r7hrc))
print(len(r7lrc))

print("Process HLT")