# Project README

This project involves processing and analyzing text data from articles. Below is a guide on how to run each file and the sequence in which they should be executed.

## Files and Their Purpose

1. **scrape_articles.py**: This script is used to scrape articles from the web and save them in `articles.txt`.
2. **stopwords_processing.py**: This file processes stopwords to clean the text data.
3. **cleaned_articles.txt**: This file contains the cleaned version of the articles after stopwords processing.
4. **text_analysis.py**: This script performs text analysis on the cleaned articles.
5. **check_files.py**: This script checks the integrity and correctness of the files generated.
6. **create_input_csv.py**: This script creates an input CSV file (`Input.csv`) from the cleaned articles.
7. **csv_operations.py**: This script performs various operations on the CSV file.
8. **convert_excel.py**: This script converts the CSV file (`Input.csv`) into an Excel file (`Input.xlsx`).

## Execution Sequence

1. **Scrape Articles**: Run `scrape_articles.py` to gather articles and save them in `articles.txt`.
   ```bash
   python scrape_articles.py
   ```

2. **Process Stopwords**: Run the stopwords processing script to clean the articles.
   ```bash
   python stopwords_processing.py
   ```

3. **Text Analysis**: Perform text analysis on the cleaned articles using `text_analysis.py`.
   ```bash
   python text_analysis.py
   ```

4. **Check Files**: Verify the integrity of the generated files using `check_files.py`.
   ```bash
   python check_files.py
   ```

5. **Create Input CSV**: Generate the input CSV file from the cleaned articles using `create_input_csv.py`.
   ```bash
   python create_input_csv.py
   ```

6. **CSV Operations**: Perform any necessary operations on the CSV file using `csv_operations.py`.
   ```bash
   python csv_operations.py
   ```

7. **Convert to Excel**: Convert the CSV file to an Excel file using `convert_excel.py`.
   ```bash
   python convert_excel.py
   ```

## Notes
- Ensure that all required dependencies are installed before running the scripts.
- Modify the scripts as needed to suit your specific requirements.
- If any script fails, check the error message and debug accordingly.
- Make sure the input files exist before running the scripts dependent on them.

