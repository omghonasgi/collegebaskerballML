import requests
import pandas as pd
from bs4 import BeautifulSoup

# URL of the website
url = "https://barttorvik.com/trank.php?year=2024&sort=&conlimit=#"

# Send a GET request to the website
response = requests.get(url)
print(response.status_code)


# Parse the content using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Assuming you want to scrape tables from the webpage
tables = pd.read_html(response.content)  # pd.read_html can parse tables directly from the response

# Inspect the first table
df = tables[0]

df.to_csv('scraped_data.csv', index=False)

# Open the file in read mode
with open('scraped_data.csv', 'r') as file:
    # Read all lines into a list
    lines = file.readlines()

# Remove the line you want to delete (e.g., the second line)
line_to_remove = 0  # Index starts from 0
del lines[line_to_remove]

# Open the file in write mode and write the remaining lines
with open('scraped_data.csv', 'w') as file:
    file.writelines(lines)

# Save or view the scraped data
stats = pd.read_csv('scraped_data.csv', index_col=0)


print(stats.head())
