from preprocessing import preprocessing
import numpy as np

def classifiy(df, roop_count = 5, dlt=True):
    pre_del = float("inf")
    df_c = df

    for _ in range(roop_count):
        mean = np.mean(df['distance(km)'])
        hhline = df.describe()['distance(km)']['75%']
        diff = abs(mean - hhline)

        if pre_del != float('inf'):
            df_c.drop(columns='class', inplace=True)

        df['class'] = np.ones(df.shape[0])

        df = df[df['distance(km)'] < diff]
        df_c.loc[df_c['distance(km)'] < diff, 'class'] = 0

        # for i in range(df.shape[0]):
        #     if df.iloc[i]['distance(km)'] > diff:
        #         df.drop(index=i, inplace=True, axis=1)

        # df.dr

        print(diff)

    if dlt:
        return df
    else:
        return df_c
