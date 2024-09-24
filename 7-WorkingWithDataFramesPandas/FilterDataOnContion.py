import pandas as pd
def filter_data_with_pd(df, column_name, condition):
    return df[df[column_name] == condition]

path =  'C:/Users/GUESTHRA/Algorithms-and-Programming-with-Phyton/data/bo_collections_data.csv'

df = pd.read_csv(path)

print(filter_data_with_pd(df, 'Release_ID', 1))
