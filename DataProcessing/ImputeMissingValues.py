import pandas as pd

def impute_missing_values(df, strategy='mean'):
    """
    Impute missing values in a dataset using the specified strategy: 'mean', 'median', or 'mode'.
    
    Parameters:
    df (pd.DataFrame): The input DataFrame with missing values.
    strategy (str): The strategy for imputation. Choose from 'mean', 'median', or 'mode'.
    
    Returns:
    pd.DataFrame: A DataFrame with missing values imputed.
    """
    if strategy not in ['mean', 'median', 'mode']:
        raise ValueError("Strategy should be 'mean', 'median', or 'mode'.")
    
    for column in df.columns:
        if df[column].dtype in ['int64', 'float64']:  # Handle numeric columns
            if strategy == 'mean':
                df[column].fillna(df[column].mean(), inplace=True)
            elif strategy == 'median':
                df[column].fillna(df[column].median(), inplace=True)
            elif strategy == 'mode':
                df[column].fillna(df[column].mode()[0], inplace=True)  # Mode returns multiple values, take the first
    return df

# Example usage
data = {
    'A': [1, 2, 3, None, 5],
    'B': [None, 2, 3, 4, 5],
    'C': [1, None, None, 4, 5]
}
df = pd.DataFrame(data)

# Impute using mean
imputed_df_mean = impute_missing_values(df.copy(), strategy='mean')
print("Mean Imputation:\n", imputed_df_mean)

# Impute using median
imputed_df_median = impute_missing_values(df.copy(), strategy='median')
print("\nMedian Imputation:\n", imputed_df_median)

# Impute using mode
imputed_df_mode = impute_missing_values(df.copy(), strategy='mode')
print("\nMode Imputation:\n", imputed_df_mode)
