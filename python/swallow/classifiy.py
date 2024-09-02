from preprocessing import distance

def classifiy(df, roop_count = 5, dlt=True):
    hhline_list = []

    for _ in range(roop_count):
        hhline = df.describe(percentiles=[.95])['distance(km)']['95%']
        hhline_list.append(hhline)

        df = df[df['distance(km)'] < hhline]

        df = df.reset_index(drop=True)
        df = distance(df)

    df.dropna(inplace=True)
    
    return df, hhline_list