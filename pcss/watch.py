import sys
import os
import time

from .process import process_sources


if __name__ == '__main__':
    path = sys.argv[1] if len(sys.argv) >= 2 else os.getcwd()
    try:
        while True:
            process_sources(path)
            time.sleep(1)
    except KeyboardInterrupt:
        pass
