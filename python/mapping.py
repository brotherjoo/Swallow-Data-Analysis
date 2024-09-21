import folium as fl

def mapping_dot(df, df_2 = None, color='blue'):
    m = fl.Map(location=(df.iloc[0]['Latitude'], df.iloc[0]['Longitude']))
    df.reset_index(inplace=True)
    df.drop(columns='index', inplace=True)
    for i in range(df.shape[0]):
        fl.Marker(
            location=(df.iloc[i]['Latitude'], df.iloc[i]['Longitude']),
            popup=f"<div><p>{df.iloc[i]['First']}</p><p>{df.iloc[i]['Latitude']}</p><p>{df.iloc[i]['Longitude']}</p></div>",
            tooltip=df.iloc[i]['First'],
            icon=fl.Icon(color=color),
        ).add_to(m)
    
    return m

def mapping_line(df, df_2):
    df['month'] = df['First'].apply(lambda x: int(x[5:7]))
    m = fl.Map(location=(
                            df[df['month'] == df['month'].unique()[0]].describe()['Latitude']['mean'],
                            df[df['month'] == df['month'].unique()[0]].describe()['Longitude']['mean']
                          )
                )
    polylist = []
    
    
    for i in df['month'].unique():
        mean_set = df[df['month'] == i].describe()
        fl.Marker(
            location=(mean_set['Latitude']['mean'], mean_set['Longitude']['mean']),
            popup=f"<div><p>{i}월</p><p>{mean_set['Latitude']['mean']}</p><p>{mean_set['Longitude']['mean']}</p></div>",
            tooltip=f"{i}월",
            icon=fl.Icon(color='red')
        ).add_to(m)

        polylist.append([mean_set['Latitude']['mean'], mean_set['Longitude']['mean']])

    fl.PolyLine(locations=polylist, color='red').add_to(m)



    df_2['month'] = df_2['First'].apply(lambda x: int(x[5:7]))
    polylist = []
    
    
    for i in df_2['month'].unique():
        mean_set = df_2[df_2['month'] == i].describe()
        fl.Marker(
            location=(mean_set['Latitude']['mean'], mean_set['Longitude']['mean']),
            popup=f"<div><p>{i}월</p><p>{mean_set['Latitude']['mean']}</p><p>{mean_set['Longitude']['mean']}</p></div>",
            tooltip=f"{i}월",
            icon=fl.Icon(color='blue')
        ).add_to(m)

        polylist.append([mean_set['Latitude']['mean'], mean_set['Longitude']['mean']])

    fl.PolyLine(locations=polylist, color='blue').add_to(m)

    return m

def mapping_d(df, df_2):
    m = fl.Map(location=(df.iloc[0]['Latitude'], df.iloc[0]['Longitude']))
    df.reset_index(inplace=True)
    df.drop(columns='index', inplace=True)
    for i in range(df.shape[0]):
        fl.Marker(
            location=(df.iloc[i]['Latitude'], df.iloc[i]['Longitude']),
            popup=f"<div><p>{df.iloc[i]['First']}</p><p>{df.iloc[i]['Latitude']}</p><p>{df.iloc[i]['Longitude']}</p></div>",
            tooltip=df.iloc[i]['First'],
            icon=fl.Icon(color='blue'),
        ).add_to(m)

    for i in range(df_2.shape[0]):
        fl.Marker(
            location=(df_2.iloc[i]['Latitude'], df_2.iloc[i]['Longitude']),
            popup=f"<div><p>{df_2.iloc[i]['First']}</p><p>{df_2.iloc[i]['Latitude']}</p><p>{df_2.iloc[i]['Longitude']}</p></div>",
            tooltip=df_2.iloc[i]['First'],
            icon=fl.Icon(color="red"),
        ).add_to(m)
    
    return m