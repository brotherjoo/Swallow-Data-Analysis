from preprocessing import preprocessing
from classifiy import classifiy
import pandas as pd

# df = pd.DataFrame(preprocessing('../../data/sample_data/data_1.txt'))
# df = classifiy(df)


df = preprocessing('/home/hyungjookim/Documents/Swallow_Data_Analysis/model_swallow/data/sample_data/data_1.txt')
df = classifiy(df)

print(df)
# print(df.shape)

