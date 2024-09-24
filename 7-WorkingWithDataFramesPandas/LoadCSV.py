import pandas as pd
def load_csv(path):
    df = pd.read_csv(path)
    return df

path = 'C:/Users/GUESTHRA/Algorithms-and-Programming-with-Phyton/data/bo_collections_data.csv'

df = load_csv(path)
print(df)
