# Mengimpor Library
import pandas as pd

# Define a dictionary containing employee data
data = {'Name': ['Leo', 'Rey', 'Bob', 'Lucy'],
        'Age': [23, 22, 25, 24],
        'Address': ['London', 'Paris', 'Bali', 'Baghdad'],
        'Qualification': ['MSC', 'MS', 'MCA', 'Phd']}

# Convert the dictionary into DataFrame
df = pd.DataFrame(data)

# Select two columns
print(df[['Name', 'Qualification']])
