import os
import pandas as pd

def divide_and_save_dataframe(df, num_parts=20, output_directory="output_parts"):
    # Create the output directory if it doesn't exist
    os.makedirs(output_directory, exist_ok=True)

    # Calculate the number of rows per part
    rows_per_part = len(df) // num_parts

    # Iterate over the parts and save each as a separate CSV file
    for i in range(num_parts):
        part_df = df[i * rows_per_part : (i + 1) * rows_per_part]
        part_file_path = os.path.join(output_directory, f"part_{i + 1}.csv")
        part_df.to_csv(part_file_path, index=False)

# Example usage:
# Divide a DataFrame into 20 parts and save them in the "output_parts" directory
csv_file = 'csv_files/track_word.csv'
df = pd.read_csv(csv_file)
divide_and_save_dataframe(df, num_parts=40, output_directory="individual_csv")
