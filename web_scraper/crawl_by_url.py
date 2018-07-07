import requests
from scrapy.http import HtmlResponse
from scrapy.linkextractors import LinkExtractor
from validators import url as is_url_valid
from urllib.parse import urlparse
import logger
log = logger.get_logger(__name__)

# Given a URL, extract the links off of that page. Each link wil be submitted to the scrape_by_url function by the main function.
def make_request(url):
    try:
        log.info('Making request for ' + url + '...')
        r = requests.get(url)
        if r.ok:
            html = r.text
            response = HtmlResponse(url=url, body=html, encoding=r.encoding)
            return response
        else:
            log.error('HTTP request failed for ' + url + ' with a ' + str(r.status_code))
            return None
    except:
        log.exception('Request failed for ' + url)
        return None


def extract_links(response):
    try:
        url_to_crawl = response.url
        log.info('Extracting links from ' + url_to_crawl + '...')
        # Make sure all links are from the current domain.
        parsed_uri_to_crawl = urlparse(url_to_crawl)
        allowed_domain = '{uri.netloc}'.format(uri=parsed_uri_to_crawl)
        # Extract links
        links = LinkExtractor(allow_domains=allowed_domain).extract_links(response)
        log.info(str(len(links)) + ' links extracted')
        urls = []
        # Process links
        for link in links:
            url = link.url
            # Remove query params
            if '?' in url:
                url = url[:url.find('?')]
            # Remove trailing slash
            url = url.strip('/')
            if url_to_crawl.strip('/') == url:
                # Do not add since that was intended to be crawled, not scraped.
                continue
            # Prevent duplicates
            if url not in urls:
                urls.append(url)
        log.info(str(len(urls)) + ' urls remain after processing')
        return urls
    # TODO: Catch specific exception for accessing response object
    # TODO: Catch specific exception for creating link extractor and extracting links
    except:
        if url_to_crawl:
            log.error('Link extraction failed for ' + url_to_crawl)
        else:
            log.error('Link extraction failed')
        return None


def crawl_by_url(url):
    # Validate URL
    if not isinstance(url, str) or not is_url_valid(url):
        log.error('Invalid URL')
        return None
    log.info('Crawler received ' + url)
    response = make_request(url)
    if response:
        links = extract_links(response)
        if links:
            return links
    log.info('No links extracted for ' + url)
    return None
