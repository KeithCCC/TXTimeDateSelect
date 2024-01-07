import pandas as pd

# Assuming 'data' is your non-DataFrame object
data = {'A': [1, 2, 3], 'B': [4, 5, 6]}

# Convert 'data' to a DataFrame
df = pd.DataFrame(data)

# Now you can use the 'append' method
new_row = {'A': 7, 'B': 8}
df = df.append(new_row, ignore_index=True)
