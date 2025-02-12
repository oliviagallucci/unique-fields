import pandas as pd

# load csv
file_path = "case_analysis_1/campaign_data/camp_full_data_history.csv"
df = pd.read_csv(file_path)

# get unique values while considering spaces and capitalization
def get_unique_values(column):
    return set(df[column].astype(str).unique())

# create dictionary to store unique values for ea header
unique_values_per_header = {col: get_unique_values(col) for col in df.columns}

# display unique values per header
print(unique_values_per_header)
