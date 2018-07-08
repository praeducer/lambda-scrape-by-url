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

Test the Lambda function:

```bash
nosetests tests/test_lambda_function.py
```

For more robust testing, you can scrape the content from a large list of URLs with the script 'urls_to_text_files.py'. It will create a plain text file for each valid URL representing the main content from each page. It will also output a file with a list of URLs where content was not extracted successfully.

```bash
python3 web_scraper/tests/urls_to_text_files.py ./web_scraper/tests/data/sample_urls_to_scrape.csv ./web_scraper/tests/results
```

## Build for Amazon Lambda

First follow these steps: https://docs.aws.amazon.com/lambda/latest/dg/with-s3-example-deployment-pkg.html#with-s3-example-deployment-pkg-python

With the addition of cloning the repo and installing all of those dependencies at once:
```bash
git clone https://github.com/praeducer/lambda-scrape-by-url
cd lambda-scrape-by-url/
./rebuild.sh
```

Then you can copy over site-packages as described in the article.

Then, instead of copying over a single file, copy everything:
```bash
zip -gr ../ScrapeByUrl.zip ./
```

You can then copy the zip file over to S3:

```bash
aws s3 cp ScrapeByUrl.zip s3://semantic-services
```

You can then add the S3 link URL, https://s3.amazonaws.com/semantic-services/ScrapeByUrl.zip, to the 'Function code' section of the 'Configuration' tab using the 'Upload a file from S3' 'Code entry type' option found here: https://console.aws.amazon.com/lambda/home?region=us-east-1#/functions/ScrapeByUrl?tab=graph

More info:

* https://docs.aws.amazon.com/lambda/latest/dg/lambda-python-how-to-create-deployment-package.html


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
