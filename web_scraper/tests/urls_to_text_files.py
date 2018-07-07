import os
import sys
import csv
from web_scraper import scrape_by_url
import time

# TODO: Refactor so code is more readable. Break up into smaller components.
# TODO: Log to a file as well as to console.
# Take in a csv of URLs and output page content to files (one per url).
# Usage: ./urls_to_text_files.py <input csv with list of urls> <directory to store output files>
# e.g. >>> python3 web_scraper/tests/urls_to_text_files.py ./web_scraper/tests/data/sample_urls_to_scrape.csv ./web_scraper/tests/results
if __name__ == '__main__':
    input_file_path = './data/sample_urls_to_scrape_short.csv'
    output_dir = './results'
    if len(sys.argv) > 1:
        input_file_path = sys.argv[1]
        print("[INFO] Input file location set to " + input_file_path)
    else:
        print("[INFO] No input file location given, defaulting to relative path " + input_file_path)
    if len(sys.argv) > 2:
        output_dir = sys.argv[2]
        print("[INFO] Output file directory set to " + output_dir)
    else:
        print("[INFO] No output file directory given, defaulting to relative path " + output_dir)
    error_file_path = output_dir + '/' + time.strftime("%Y%m%d-%H%M%S-") + "urls-with-no-output.log"
    current_url_index = 0
    url_count = 0
    success_count = 0
    url = None
    if os.path.exists(input_file_path):
        with open(input_file_path) as csv_file:
            if os.path.exists(output_dir):
                with open(error_file_path, "w") as error_file:
                    try:
                        print("[INFO] Successfully opened " + input_file_path)
                        url_reader = csv.reader(csv_file)
                        print("[INFO] Successfully read " + input_file_path)
                        # Note: Iterating over entire file twice.
                        # Though this is not performant, it is useful for reporting. Comment out next two lines to scale.
                        url_count = sum(1 for row in url_reader)
                        csv_file.seek(0)
                        for url_arg in url_reader:
                            current_url_index += 1
                            url = url_arg[0]
                            print("[INFO] (" + str(current_url_index) + "/" + str(url_count) + ") Attempting to extract content from " + url + "...")
                            content = scrape_by_url(url)
                            if content:
                                success_count += 1
                                output_file_name = ''.join(e for e in url if e.isalnum())
                                if len(output_file_name) > 255:
                                    output_file_name = output_file_name[-255:]
                                output_file_path = output_dir + '/' + output_file_name + '.txt'
                                if len(output_file_path) <= 260:
                                    with open(output_file_path, mode='w') as output_file:
                                        print("[INFO] (" + str(current_url_index) + "/" + str(url_count) + ") Writing content of " + url + " to " + output_file_path + "...")
                                        output_file.write(content)
                                else:
                                    print("[ERROR] Unable to write file due to path length exceeding 260 characters: " + output_file_path)
                                    error_file.write("ERROR_WRITING," + url + "\n")
                            else:
                                print("[ERROR] No content returned for " + url)
                                if content is None:
                                    error_file.write("ERROR_EXTRACTING," + url + "\n")
                                elif content.isspace() or content == '':
                                    error_file.write("EMPTY_CONTENT," + url + "\n")
                                else:
                                    error_file.write("ERROR," + url + "\n")
                    except Exception as e:
                        print(e)
                        print("[ERROR] A failure occurred while reading or processing " + input_file_path)
                        if url:
                            print("[ERROR] Last url read was " + url)
            else:
                print("[ERROR] The path to the output directory " + output_dir + " was not found")
    else:
        print("[ERROR] The path to the input file " + input_file_path + " was not found")
    print("[INFO] Script completed with a final success ratio of " + str(success_count) + "/" + str(
        url_count) + "")
