import requests
import pandas as pd
from bs4 import BeautifulSoup

# URL of the website
url = "https://barttorvik.com/trank.php#"

# Send a GET request to the website
response = requests.get(url)

# Parse the content using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Assuming you want to scrape tables from the webpage
tables = pd.read_html(response.content)  # pd.read_html can parse tables directly from the response

# Inspect the first table
df = tables[0]

df.to_csv('scraped_data.csv', index=False)

# Save or view the scraped data
print(df.head())