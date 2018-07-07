import os
import sys
import csv
from web_scraper import crawl_by_url
import time

# TODO: Refactor so code is more readable. Break up into smaller components.
# TODO: Log to a file as well as to console.
# Take in a csv of URLs and output all URLs on those pages to a file.
# Usage: ./urls_to_urls_file.py <input csv with list of urls> <directory to store output file>
# e.g. >>> python3 web_scraper/tests/urls_to_urls_file.py ./web_scraper/tests/data/sample_urls_to_crawl.csv ./web_scraper/tests/results/crawl
if __name__ == '__main__':
    input_file_path = './data/sample_urls_to_crawl_short.csv'
    output_dir = './results/crawl'
    if len(sys.argv) > 1:
        input_file_path = sys.argv[1]
        print('[INFO] Input file location set to ' + input_file_path)
    else:
        print('[INFO] No input file location given, defaulting to relative path ' + input_file_path)
    if len(sys.argv) > 2:
        output_dir = sys.argv[2]
        print('[INFO] Output file directory set to ' + output_dir)
    else:
        print('[INFO] No output file directory given, defaulting to relative path ' + output_dir)
    error_file_path = output_dir + '/crawling-results-failure-urls-' + time.strftime('%Y%m%d-%H%M%S') + '.log'
    output_file_path = output_dir + '/crawling-results-' + time.strftime('%Y%m%d-%H%M%S') + '.txt'
    current_url_index = 0
    url_count = 0
    success_count = 0
    output_url_count = 0
    url = None
    if os.path.exists(input_file_path):
        with open(input_file_path) as csv_file:
            if os.path.exists(output_dir):
                with open(error_file_path, 'w') as error_file:
                    with open(output_file_path, mode='w') as output_file:
                        try:
                            print('[INFO] Successfully opened ' + input_file_path)
                            url_reader = csv.reader(csv_file)
                            print('[INFO] Successfully read ' + input_file_path)
                            # Note: Iterating over entire file twice.
                            # Though this is not performant, it is useful for reporting. Comment out next two lines to scale.
                            url_count = sum(1 for row in url_reader)
                            csv_file.seek(0)
                            for url_arg in url_reader:
                                current_url_index += 1
                                url = url_arg[0]
                                print('[INFO] (' + str(current_url_index) + '/' + str(url_count) + ') Attempting to crawl ' + url + '...')
                                urls = crawl_by_url(url)
                                if urls and len(urls) > 0:
                                    success_count += 1
                                    print('[INFO] (' + str(current_url_index) + '/' + str(url_count) + ') Writing urls of ' + url + ' to ' + output_file_path + '...')
                                    for output_url in urls:
                                        output_file.write(output_url + '\n')
                                        output_url_count += 1
                                else:
                                    print('[ERROR] No urls returned for ' + url)
                                    if urls is None:
                                        error_file.write('ERROR_EXTRACTING,' + url + '\n')
                                    elif urls == []:
                                        error_file.write('EMPTY_LIST,' + url + '\n')
                                    else:
                                        error_file.write('UNKNOWN_ERROR,' + url + '\n')
                        except Exception as e:
                            print(e)
                            print('[ERROR] A failure occurred while reading or processing ' + input_file_path)
                            if url:
                                print('[ERROR] Last url read was ' + url)
            else:
                print('[ERROR] The path to the output directory ' + output_dir + ' was not found')
    else:
        print('[ERROR] The path to the input file ' + input_file_path + ' was not found')
    print('[INFO] ' + str(success_count) + ' out of ' + str(url_count) + ' urls were crawled successfully.')
    print('[INFO] A total of ' + str(output_url_count) + ' urls were extracted successfully.')
