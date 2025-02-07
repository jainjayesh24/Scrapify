import csv

# Define the CSV file path
csv_file_path = "Input.csv"

# List of URLs to include in the CSV file
urls = [
    ("1", "https://www.nytimes.com/2020/09/02/opinion/remote-learning-coronavirus.html", "Opinion"),
    ("2", "https://www.washingtonpost.com/technology/2020/09/25/privacy-check-blacklight/", "Technology"),
    ("3", "https://edition.cnn.com/travel/article/scenic-airport-landings-2020/index.html", "Travel"),
    ("4", "https://www.reuters.com/article/us-health-coronavirus-global-deaths/global-coronavirus-deaths-pass-agonizing-milestone-of-1-million-idUSKBN26K08Y", "Health")
]

# Create and write to the CSV file
with open(csv_file_path, mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    # Write the header
    writer.writerow(["ID", "URL", "Category"])
    # Write the data
    writer.writerows(urls)

print(f"File '{csv_file_path}' has been created successfully!")
