import pandas as pd

# Load the data
df = pd.read_csv('data/jira_issues.csv')

# Print the columns
print("Columns in CSV file:", df.columns)
