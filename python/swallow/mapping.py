import folium as fl

def mapping(df, dot=True, line=True):
    m = fl.Map(location=(df.iloc[0]['Latitude'], df.iloc[0]['Longitude']))
    df.reset_index(inplace=True)
    df.drop(columns='index', inplace=True)

    if dot:
        for i in range(df.shape[0]):
            fl.Marker(
                location=(df.iloc[i]['Latitude'], df.iloc[i]['Longitude']),
                popup=f"<div><p>{df.iloc[i]['First']}</p><p>{df.iloc[i]['Latitude']}</p><p>{df.iloc[i]['Longitude']}</p></div>",
                tooltip=df.iloc[i]['First']
            ).add_to(m)

    if line:
        list_line = []
        for i in range(df.shape[0]):
            list_line.append([df.iloc[i]['Latitude'], df.iloc[i]['Longitude']])
        
        fl.PolyLine(list_line).add_to(m)
    
    return m