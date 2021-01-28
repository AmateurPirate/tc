import time
import pandas as pd

limit = 10**4+1
interval = 100

cols = [x for x in range(1, limit, interval)]

df = pd.DataFrame(columns=cols)

def N_tc(x):
    for _ in range(x):
        pass
    return

def N2_tc(x):
    for _ in range(x):
        for _ in range(x):
            pass
        return

def logN_tc(x):
    while x >= 1:
        x /= 2
    return

def Nlog_N_tc(x):
    for i in range(x):
        while i >= 1:
            i /= 2
    return

def one_tc(x):
    return

def one_million_tc(x):
    for _ in range(10**6):
        pass
    return

myfuncs = [N_tc, N2_tc, logN_tc, Nlog_N_tc, one_tc, one_million_tc]

cols_set = set(cols)

for func in myfuncs:
    times = []
    for x in range(limit):
        if x in cols_set:
            s = time.time()
            ans = func(x)
            times.append(time.time() - s)

    data = {x: y for x, y in zip(cols, times)}


    
    df = df.append(data, ignore_index=True)

print(df)
