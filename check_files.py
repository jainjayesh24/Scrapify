import os

file_path = "Input.csv"

if os.path.exists(file_path):
    print(f"✅ {file_path} exists!")
else:
    print(f"❌ {file_path} is missing! Run convert_excel.py first.")
