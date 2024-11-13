import requests
import pandas as pd
from bs4 import BeautifulSoup

class WebScraper:
    def __init__(self, url):
        # URL of the website
        self.url = url

    def get_data(self):
        # Send a GET request to the website
        response = requests.get(self.url)

        # Parse the content using BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')

        # Assuming you want to scrape tables from the webpage
        tables = pd.read_html(response.content)  # pd.read_html can parse tables directly from the response

        # Inspect the first table and remove the first row
        table = tables[0].iloc[1:]  # Skip the first row

        # Specify columns that may contain extra ranking values after the main statistic
        columns_to_clean = table.columns[5:]  # Adjust column index as needed

        # Clean each column by removing rankings and converting to numeric
        for col in columns_to_clean:
            # Remove ranking or text after spaces
            table[col] = table[col].str.split().str[0]

            # Convert to numeric, setting errors='coerce' to handle any remaining non-numeric values
            table[col] = pd.to_numeric(table[col], errors='coerce')
        

        # Save or view the scraped data
        table.to_csv('scraped_data.csv', index=False)

        # Load the data from CSV to verify
        stats = pd.read_csv('scraped_data.csv', index_col=0)
        return stats
