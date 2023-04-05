import logging

logging.basicConfig(
    level=logging.DEBUG,
    filename='logger.log',
    format='%(asctime)s -,- %(levelname)s -,- %(name)s -,- %(message)s',
    filemode="a",
)

logging.info('The logger alive')