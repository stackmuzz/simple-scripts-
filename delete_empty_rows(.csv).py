# import pandas as pd
#
# # Replace 'Maine_Well_Database_-_Well_Depth.csv' with your CSV file path
# file_path = r'C:\Users\Amrendra pratapsingh\Downloads\Maine_Well_Database_-_Well_Depth.csv'
#
# # Read the CSV file into a DataFrame
# df = pd.read_csv(file_path)
#
# # Remove rows that are completely empty
# df.dropna(how='all', inplace=True)
#
# # Write the cleaned DataFrame back to the CSV file
# df.to_csv(file_path, index=False)
import pandas as pd

# Replace 'Maine_Well_Database_-_Well_Depth.csv' with your CSV file path
file_path = r'C:\Users\Amrendra pratapsingh\Downloads\Maine_Well_Database_-_Well_Depth.csv'

# Read the CSV file into a DataFrame
df = pd.read_csv(file_path, low_memory=False)

# Remove rows that have all columns empty or NaN
df.dropna(axis=0, how='all', inplace=True)

# Specify the path for the cleaned CSV file
cleaned_file_path = r'C:\Users\Amrendra pratapsingh\Desktop\SIH\python scripts\cleaned_data.csv'

# Write the cleaned DataFrame to the new CSV file
df.to_csv(cleaned_file_path, index=False)

print("Empty rows removed, cleaned data saved to 'cleaned_data.csv'")