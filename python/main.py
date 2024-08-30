from modules.preprocessing import preprocessing
import pandas as pd

df = preprocessing(input())
name = input()
df.to_csv(f'./data/save_data/{name}', na_rep="NaN", sep=",")