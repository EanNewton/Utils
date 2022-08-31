#!/usr/bin/python3

from constants import DEFAULT_DIR
from math import ceil


# TODO Docstrings not auto-generating anymore for some reason, find plugin?
def insertion_sort(raw: list) -> list:
    """

    """
    for each in range(1, len(raw)):
        key = raw[each]
        j = each - 1
        while j >= 0 and key < raw[j]:
            # We need to swap elements
            raw[j + 1] = raw[j]
            j -= 1
            raw[j + 1] = key

def chunk(lst: list, size: int) -> list:
    """
    Chunk a lst into smaller lists of size.
    Use range to create a list of desired size then use map on it to fill it with splices of lst.
    """
    return list(map(lambda _: lst[_ * size : _ * size + size], list(range(0, ceil(len(lst) / size)))))


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


def fetch_file(directory:str, filename:str):
    """Safely read in a dynamically designated local file"""
    with open('{}/docs/{}/{}.txt'.format(DEFAULT_DIR, directory, filename), 'r') as f:
        return f.read()


def wrap(long_string:str, max_length:int) -> list:
    """Break a long string into a list of strings of no more than max_length"""
    return [long_string[i:i + max_length] for i in range(0, len(long_string), max_length)]
