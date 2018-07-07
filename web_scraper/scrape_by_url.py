from newspaper import Article, fulltext
from validators import url as is_url_valid
import logger
log = logger.get_logger(__name__)

# Given a URL, scrape the main content from the page.
def scrape_by_url(url):
    # TODO: Handle specific errors
    try:
        # Validate URL
        if not isinstance(url, str) or not is_url_valid(url):
            log.error('Invalid URL')
            return None
        # Extract Content
        article = Article(url)
        article.download()
        # TODO: Only attempt parse if download is successful
        article.parse()
        article_text = article.text
        if article_text and not article_text.isspace():
            return article_text
        page_text = fulltext(article.html)  # html = requests.get(...).text
        if page_text:
            if page_text.isspace() or page_text == '':
                return ''
            return page_text
    except Exception as e:
        log.error('Content extraction failed for ' + url)
    return None
