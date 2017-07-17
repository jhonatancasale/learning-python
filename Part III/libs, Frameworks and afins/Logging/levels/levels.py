#!env python3
# -*- coding: utf-8 -*-
'''Logging level messages example'''
# from https://www.youtube.com/watch?v=g8nQ90Hk328

import logging

LOG_FORMAT = '%(asctime)s:%(levelname)s:%(message)s'
logging.basicConfig(filename = 'levels.log',
                    level = logging.DEBUG,
                    format = LOG_FORMAT,
                    filemode = 'w'
                   )

logger = logging.getLogger()

def main():
    '''Logging level messages example'''

    logger.debug('This is a harmless debug message.')
    logger.info('Just some useful info.')
    logger.warning("I'm sorry, but I can't do that, Dave.")
    logger.error('Did you just try to divide by zero?')
    logger.critical('The entire internet is down!!')

if __name__ == '__main__':
    main()
