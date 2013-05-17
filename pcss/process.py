import sys
import os
from collections import defaultdict

file_times = defaultdict(float)


def process_sources(path):
    for dirpath, dirnames, filenames in os.walk(path):
        sources = [f for f in filenames if f.endswith('.css.py')]
        for src in sources:
            src_path = os.path.join(dirpath, src)
            src_stat = os.stat(src_path)
            if src_stat.st_mtime > file_times[src_path]:
                file_times[src_path] = src_stat.st_mtime
                print "processing file", src_path
                os.system('python %s > %s' % (src_path,
                    os.path.join(dirpath, src.replace('.css.py', '.css'))))


if __name__ == '__main__':
    path = sys.argv[1] if len(sys.argv) >= 2 else os.getcwd()
    process_sources(path)
