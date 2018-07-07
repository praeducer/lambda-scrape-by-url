# lambda-scrape-by-url
Given a URL, scrape the main content from the page. Configured for AWS Lambda.

## Setup the Web Scraper Package

From the root of the project directory, run this to install all dependencies and (re)install the web_scraper package (this is similar to 'pip3 install -r requirements.txt' except the custom package will be reinstalled each time it is ran):

```bash
pip3 install -e .
```

Or:

```bash
./rebuild.sh
```

## Test the Web Scraper Package

Install 'nose':

```bash
pip3 install nose
```

Run the test class:

```bash
nosetests web_scraper/tests/test_web_scraper.py
```

For more robust testing, you can scrape the content from a large list of URLs with the script 'urls_to_text_files.py'. It will create a plain text file for each valid URL representing the main content from each page. It will also output a file with a list of URLs where content was not extracted successfully.

```bash
python3 web_scraper/tests/urls_to_text_files.py ./web_scraper/tests/data/sample_urls_to_scrape.csv ./web_scraper/tests/results
```

## Troubleshooting

### Python Packaging

If you make changes to the module, run 'rebuild.sh' to update the module in your env before running tests.

If you do not have permission to run shell scripts, run this first:

```bash
sudo chmod 755 rebuild.sh
```

If your IDE is failing to recognize the requirements, you may also try this (though it may be redundant):

```bash
python3 setup.py develop
```

### Testing

If you are on macOS, you may need to execute these steps before installing 'nose':

```bash
sudo mkdir -p /usr/local/man
sudo chown -R "$USER:admin" /usr/local/man
```
