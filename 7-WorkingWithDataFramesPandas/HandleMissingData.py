import pandas as pd
def handle_missing_data_with_pd(df):
    return df.dropna()

path =  'C:/Users/GUESTHRA/Algorithms-and-Programming-with-Phyton/data/bo_collections_data.csv'

df = pd.read_csv(path)

print(handle_missing_data_with_pd(df))