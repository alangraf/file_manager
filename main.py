import os
from log import Logger
from time import sleep
from os.path import join
from manager import FileManager
from termcolor import colored
from dirs import DIRS_TO_CLEAN

logg = Logger()
HOME_DIRECTORY = os.path.expanduser('~')
TARGET_PATH = join(HOME_DIRECTORY, DIRS_TO_CLEAN[0])
DIR_ROOTS = [join(HOME_DIRECTORY, d) for d in DIRS_TO_CLEAN]

if __name__ == '__main__':
    try:
        logg.info('File Manager started')
        logg.info('Watchdog is activated')

        while True:
            sleep(1)
            FileManager(DIR_ROOTS, TARGET_PATH, logg).run()
    except KeyboardInterrupt as interrupt:
        print(interrupt)