#!/usr/bin/env python3
"""
Module Docstring
"""

__author__ = "EanNewton"
__version__ = "0.1.0"
__license__ = "AGPL-3.0"

import argparse
from contextlib import contextmanager
from subprocess import Popen
from os import getpid
from signal import SIGINT
from time import sleep, time
from resource import getrusage, RUSAGE_SELF


from logzero import logger


DEFAULT_DIR = path.dirname(path.abspath(__file__))
VERBOSE = 1
events = [
    "instructions",
    "cache-references",
    "cache-misses",
    "avx_insts.all",
]


@contextmanager
def perf():
    """Benchmark this process with Linux's perf util.

    Example usage:

        with perf():
            x = run_some_code()
            more_code(x)
            all_this_code_will_be_measured()
    """
    p = Popen([
        # Run perf stat
        "perf", "stat",
        # for the current Python process
        "-p", str(getpid()),
        # record the list of events mentioned above
        "-e", ",".join(events)])
    # Ensure perf has started before running more
    # Python code. This will add ~0.1 to the elapsed
    # time reported by perf, so we also track elapsed
    # time separately.
    sleep(0.1)
    start = time()
    try:
        yield
    finally:
        print(f"Elapsed (seconds): {time() - start}")
        print("Peak memory (MiB):",
              int(getrusage(RUSAGE_SELF).ru_maxrss / 1024))
        p.send_signal(SIGINT)


def main(args):
    """ Main entry point of the app """
    logger.info("hello world")
    logger.info(args)

    

def wikisearch(query: str) -> str:
    """
    Searches the RimWorld wiki for content.
    :type query: str
    """
    queryAddress = "http://rimworldwiki.com/api.php?action=query&list=search&format=json&srlimit=5&srprop=size|wordcount|timestamp&srsearch={0}";

    banner = None
    return banner

def debug(func):
    """Print the function signature and return value"""
    if VERBOSE >= 1:
        @functools.wraps(func)
        def wrapper_debug(*args, **kwargs):
            args_repr = [repr(a) for a in args]
            kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
            signature = ", ".join(args_repr + kwargs_repr)

            print(f"Calling {func.__name__}({signature})\n")
            value = func(*args, **kwargs)
            print(f"{func.__name__!r} returned {value!r}\n")

            return value

        return wrapper_debug
    else:
        return func
    
    
def timer(func):
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        tic = time.perf_counter()
        value = func(*args, **kwargs)
        toc = time.perf_counter()
        elapsed_time = toc - tic
        print(f"Elapsed time: {elapsed_time:0.4f} seconds")
        return value
    return wrapper_timer


def multi_in() -> list:
    """
    Take input containing line breaks as single input.
    :return: list
    """
    lines = []
    while True:
        line = input()
        if line:
            lines.append(line)
        else: break
    return lines


def fetch_file(directory, filename):
    """Safely read in a dynamically designated local file"""
    with open('{}/docs/{}/{}.txt'.format(DEFAULT_DIR, directory, filename), 'r') as f:
        return f.read()


def wrap(s, w):
    """Break a long string s into a list of strings of length w"""
    return [s[i:i + w] for i in range(0, len(s), w)]


def matrix_rotate(raw: list) -> list:
    """Rotate elements in a list of lists by 90 degrees, ie columns -> rows"""
    return [[_[each] for _ in raw] for each in range(len(raw[0]))]


def flatten_lists(list_of_lists: list) -> list:
    return [item for sublist in list_of_lists for item in sublist]


if __name__ == '__main__':
    print(globals()['d' + input('> ')](input('>> ')))  # ENTER to EOF
    # print(globals()['d' + input('>')](multi_in()))  # ENTER to EOF
    # print(globals()['d'+input('>')](sys.stdin.readlines())) # Ctrl-D to EOF
    # print(globals()['d' + input('>')](open(0).read()))  # Ctrl-D to EOF

if __name__ == "__main__":
    """ This is executed when run from the command line """
    parser = argparse.ArgumentParser()

    # Required positional argument
    parser.add_argument("arg", help="Required positional argument")

    # Optional argument flag which defaults to False
    parser.add_argument("-f", "--flag", action="store_true", default=False)

    # Optional argument which requires a parameter (eg. -d test)
    parser.add_argument("-n", "--name", action="store", dest="name")

    # Optional verbosity counter (eg. -v, -vv, -vvv, etc.)
    parser.add_argument(
        "-v",
        "--verbose",
        action="count",
        default=0,
        help="Verbosity (-v, -vv, etc)")

    # Specify output of "--version"
    parser.add_argument(
        "--version",
        action="version",
        version="%(prog)s (version {version})".format(version=__version__))

    args = parser.parse_args()
    main(args)

if __name__ == '__main__':
    help = """
    Cell Automata.

    Usage:
        Conways Game of Life
        ====================
        main.py conway
        main.py conway <filename>
        main.py conway <width> <height> <density>
    Options:
        <filename> -- a .txt file located in ./pregens
        <width>    -- X cell range
        <height>   -- Y cell range
        <density>  -- percent chance to spawn a living cell at start, between 0 and 100
    """
    if 'help' in argv:
        print(help)
        quit()

    elif len(argv) >= 2:
        if argv[1] == 'conway':
            if len(argv) == 3:
                board = load_file(argv[2])
                board = expand_board(board, 50, 25)
            elif len(argv) == 5:
                board = random_state(int(argv[2]), int(argv[3]), int(argv[4]))
            else:
                board = random_state(50, 25, 50)
            conway(board)
    print(help)
