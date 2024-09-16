import pandas as pd
def calculate_summary_statistics_with_pd(df):
    return df.describe()

path =  'C:/Users/GUESTHRA/Algorithms-and-Programming-with-Phyton/data/bo_collections_data.csv'

df = pd.read_csv(path)

print(calculate_summary_statistics_with_pd(df))