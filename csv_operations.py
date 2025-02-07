import pandas as pd

csv_file = "Input.csv"

try:
    df = pd.read_csv(csv_file)
    print("CSV Content:\n", df.head())
except FileNotFoundError:
    print(f"Error: {csv_file} not found. Run convert_excel.py first.")
