from setuptools import setup
setup(name='lambda-scrape-by-url',
      version='0.0.1',
      description='AWS Lambda Function that scrapes a web page given a URL',
      url='https://github.com/praeducer/lambda-scrape-by-url',
      author='Paul Prae',
      author_email='',
      license='None',
      packages=['web_scraper'],
      install_requires=[
            'newspaper3k',
            'validators',
            'Scrapy',
            'requests'
      ],
      test_suite='nose.collector',
      tests_require=['nose'],
      zip_safe=False)
