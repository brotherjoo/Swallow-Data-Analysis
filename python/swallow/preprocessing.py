import pandas as pd
from haversine import haversine

def distance(df):
    list_temp = []

    for i in range(df.shape[0]-2):
        list_temp.append(haversine(df.iloc[i]['Latitude'], df.iloc[i]['Longitude'], df.iloc[i+1]['Latitude'], df.iloc[i+1]['Longitude']))  ## index 1 ~ index 691 까지

    temp = pd.Series(list_temp, name="distance(km)")

    df = df.drop(columns='distance(km)')
    df = pd.concat([df, temp], axis=1)

    return df

def preprocessing(link, save=False, to_link=None):
    df = pd.read_csv(link, sep="\t", encoding='cp949', index_col=0)
    
    list_temp = []

    for i in range(df.shape[0]-2):
        list_temp.append(haversine(df.iloc[i]['Latitude'], df.iloc[i]['Longitude'], df.iloc[i+1]['Latitude'], df.iloc[i+1]['Longitude']))  ## index 1 ~ index 691 까지

    temp = pd.Series(list_temp, name="distance(km)")

    df_c = df.drop(index=0, axis=0)
    df.drop(index=df.shape[0]-1, inplace=True)

    df_c.reset_index(inplace=True)

    df['Longitude_difference'] = df['Longitude'] - df_c['Longitude']
    df['Latitude_difference'] = df['Latitude'] - df_c['Latitude']

    df.drop(index=0, inplace=True)

    df.reset_index(inplace=True)

    df = pd.concat([df, temp], axis=1)
    df.drop(columns=['Index', 'Quality_1', 'Second', "Quality_2", 'ElevAngle', 'Type'], inplace=True)

    df.dropna(inplace=True)
    df.reset_index(inplace=True)

    df.drop(columns='index', inplace=True)

    if save:
        df.to_csv(to_link, encoding='cp949')

    return df
