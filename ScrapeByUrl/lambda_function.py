from web_scraper import scrape_by_url
import logger
log = logger.get_logger(__name__)
def lambda_handler(event, context):
    try:
        url = event["url"]
    except Exception as e:
        message = "Error: url for scraping is not present in the message."
        log.debug(message)
        result = {
            "url": None,
            "content": None,
            "message": message
        }
        return result
    content = scrape_by_url(url)
    if content != None:
        result = {
            "url": url,
            "content": content,
            "message": "Content extracted from web page successfully."
        }
    else:
        result = {
            "url": url,
            "content": None,
            "message": "Content extraction failed."
        }
    return result
