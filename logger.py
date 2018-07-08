import logging

logging.basicConfig(filename='web_scrapper.log', format='[%(levelname)s] - [%(asctime)s] -[%(name)s]  %(message)s',
                    level=logging.INFO)

console = logging.StreamHandler()
console.setLevel(logging.DEBUG)

# set a format which is simpler for console use
formatter = logging.Formatter('[%(levelname)s] [%(name)s] %(message)s')
console.setFormatter(formatter)

# add the handler to the root logger
logging.getLogger('').addHandler(console)


def get_logger(name):
    return logging.getLogger(name)