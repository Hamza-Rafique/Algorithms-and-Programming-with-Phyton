import numpy as np
import pandas as pd

# 1. Set the seed for reproducibility
np.random.seed(42)

# 2. Define the number of rows for the dataset
num_rows = 1000

# 3. Generate synthetic data (features)
customer_ids = np.arange(1, num_rows + 1)  # Unique customer IDs
ages = np.random.randint(18, 70, size=num_rows)  # Random ages between 18 and 70
incomes = np.random.randint(30000, 120000, size=num_rows)  # Random annual income
genders = np.random.choice(['Male', 'Female'], size=num_rows)  # Random gender
purchase_amounts = np.round(np.random.uniform(10.5, 5000.75, size=num_rows), 2)  # Purchase amounts

# 4. Create a Pandas DataFrame with the generated data
df = pd.DataFrame({
    'CustomerID': customer_ids,
    'Age': ages,
    'Income': incomes,
    'Gender': genders,
    'PurchaseAmount': purchase_amounts
})

# 5. Save the DataFrame to a CSV file
csv_file = 'synthetic_customer_data.csv'
df.to_csv(csv_file, index=False)

print(f"Synthetic data saved to {csv_file}")
