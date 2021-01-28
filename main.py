import time
import pandas as pd
import matplotlib.pyplot as plt

limit = 10**4+1
interval = 100

class make_functions:
    def __init__(self):
        pass
    def self.N_tc(self, x):
        for _ in range(x):
            pass
        return

    def self.N2_tc(self, x):
        for _ in range(x):
            for _ in range(x):
                pass
            return

    def self.logN_tc(self, x):
        while x >= 1:
            x /= 2
        return

    def self.Nlog_N_tc(self, x):
        for i in range(x):
            while i >= 1:
                i /= 2
        return

    def self.one_tc(self, x):
        return

    def self.one_million_tc(self, x):
        for _ in range(10**6):
            pass
        return


class make_df:
    def __init__(self, limit, interval):
        mf = make_functions()
        self.myfuncs = [mf.N_tc, mf.N2_tc, mf.logN_tc, mf.Nlog_N_tc, mf.one_tc, mf.one_million_tc]
        self.cols = [x for x in range(1, limit, interval)]
        self.cols_set = set(self.cols)
        self.df = self.gen_df()

    def gen_df(self):
        df = pd.DataFrame(columns=cols)

        for func in self.myfuncs:
            times = []
            for x in range(limit):
                if x in self.cols_set:
                    s = time.time()
                    ans = func(x)
                    times.append(time.time() - s)

            data = {x: y for x, y in zip(cols, times)}

            df = df.append(data, ignore_index=True)
        return df


class plot_df:
    def __init__(self, limit, interval):
        mdf = make_df(limit, interval)
        self.df = mdf.gen_df()
    def plot(self):
        ax = plt.gca()

        self.df.plot(kind='line',x='name',y='num_children',ax=ax)
        self.df.plot(kind='line',x='name',y='num_pets', color='red', ax=ax)

        plt.show()

def main():
    pass


if __name__ == '__main__':
    DEBUG = False

    if DEBUG:
        pass
    else:
        main()


ax = plt.gca()

df.plot(kind='line',x='name',y='num_children',ax=ax)
df.plot(kind='line',x='name',y='num_pets', color='red', ax=ax)

plt.show()
