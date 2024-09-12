import pandas as pd

def group_by_column_with_pd(df, column_name):
    return df.groupby(column_name)

path =  'C:/Users/GUESTHRA/Algorithms-and-Programming-with-Phyton/data/bo_collections_data.csv'

df = pd.read_csv(path)

print(group_by_column_with_pd(df, 'Release_ID'))

