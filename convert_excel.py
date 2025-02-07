import pandas as pd

# Read Excel file
excel_file = "Input.xlsx"
csv_file = "Input.csv"

try:
    df = pd.read_excel(excel_file)
    df.to_csv(csv_file, index=False)
    print(f"Converted {excel_file} to {csv_file} successfully!")
except FileNotFoundError:
    print(f"Error: {excel_file} not found. Please add the Excel file.")
