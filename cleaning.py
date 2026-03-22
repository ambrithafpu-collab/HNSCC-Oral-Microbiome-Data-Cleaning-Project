import pandas as pd

# Load dataset
data = pd.read_csv("data.csv")

# Show original data
print("Original Data:")
print(data)

# Remove missing values
clean_data = data.dropna()

# Save cleaned data
clean_data.to_csv("cleaned_data.csv", index=False)

print("\nCleaned Data:")
print(clean_data)
