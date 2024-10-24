from webscraper import WebScraper

def main():
    scraper = WebScraper("https://barttorvik.com/trank.php?year=2024&sort=&conlimit=#")
    data = scraper.get_data()
    print(data.dtypes)

main()