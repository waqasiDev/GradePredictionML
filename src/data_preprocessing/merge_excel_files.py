import pandas as pd
import os

# Folder containing Excel files
input_folder = 'data/raw/complete_data'

# List to hold data from all Excel files
all_data = []

# Loop through all Excel files in the directory
for file_name in os.listdir(input_folder):
    if file_name.endswith('.xlsx'):  # Check if the file is an Excel file
        file_path = os.path.join(input_folder, file_name)
        
        # Read the current Excel file into a DataFrame
        df = pd.read_excel(file_path)
        
        # Optionally, you can add a column to track the source file
        # df['Source File'] = file_name
        
        # Append the data to the list
        all_data.append(df)

# Concatenate all the DataFrames into one
merged_data = pd.concat(all_data, ignore_index=True)

# Save the merged data to a new Excel file
output_file = 'data/raw/merged_data.xlsx'
merged_data.to_excel(output_file, index=False)

print(f"Merged data saved to: {output_file}")
