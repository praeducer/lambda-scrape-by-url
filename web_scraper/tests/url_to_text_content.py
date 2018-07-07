import sys
from web_scraper import scrape_by_url

# Prints out the content from the page found at a single URL passed in as a cmd line arg
if __name__ == '__main__':
    if len(sys.argv) > 1:
        print(scrape_by_url(sys.argv[1]))
    else:
        print(scrape_by_url('http://www-03.ibm.com/press/us/en/pressrelease/53622.wss'))
