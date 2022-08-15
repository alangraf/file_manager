import os
import time
from os.path import join
from manager import FileManager
from termcolor import colored

HOME_DIRECTORY = os.path.expanduser('~')
DIRS_TO_CLEAN = ['Downloads']
TARGET_PATH = join(HOME_DIRECTORY, DIRS_TO_CLEAN[0])
DIR_ROOTS = [join(HOME_DIRECTORY, d) for d in DIRS_TO_CLEAN]

if __name__ == '__main__':
    try:
        print(colored('\nFile Manager started...', 'green'))

        while True:
            time.sleep(2)
            FileManager(DIR_ROOTS, TARGET_PATH).run()
    except KeyboardInterrupt as interrupt:
        print(interrupt)