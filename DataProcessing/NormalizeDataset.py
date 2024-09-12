import pandas as pd

def normalize(df):
    """
    Normalize the values in a dataset (Pandas DataFrame) between 0 and 1 using Min-Max scaling.
    
    Parameters:
    df (pd.DataFrame): The input DataFrame to normalize.
    
    Returns:
    pd.DataFrame: A DataFrame with values normalized between 0 and 1.
    """
    return (df - df.min()) / (df.max() - df.min())

data = {
    'A': [10, 20, 30, 40, 50],
    'B': [15, 25, 35, 45, 55],
    'C': [100, 200, 300, 400, 500]
}
df = pd.DataFrame(data)
print("Original DataFrame:\n", df)

normalized_df = normalize(df)
print("Normalized DataFrame:\n", normalized_df)
