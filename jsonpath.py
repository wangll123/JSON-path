#!/usr/bin/env python3

"""
Find the path of a key / value in a JSON hierarchy easily.

It was made for JSON files, but it also works with dictionaries,
of course.

Inspired by:
* http://stackoverflow.com/a/34837235/232485 (doesn't treat nested lists)
* http://chris.photobooks.com/json/default.htm (in-browser visualization)

Author:
* Laszlo Szathmary, alias Jabba Laci, 2017, jabba.laci@gmail.com
"""

import json
import sys
from typing import Dict, List, Union, Any


def traverse(path: str, obj: Union[Dict, List]) -> None:
    """
    Traverse the object recursively and print every path / value pairs.
    """
    if isinstance(obj, list):
        for i, subnode in enumerate(obj):
            traverse(path + f'[{i!r}]', subnode)
    elif isinstance(obj, dict):
        for k, v in obj.items():
            traverse(path + f'[{k!r}]', v)
    else:
        print(path + ' => ' + f'{obj!r}')


def read_file(fpath: str) -> Dict:
    """
    Read the JSON file and return its content as a Python data structure.
    """
    with open(fpath) as f:
        return json.load(f)    # type: ignore


def process(fname: str) -> None:
    """
    Process the given JSON file.
    """
    d: Dict = read_file(fname)
    traverse("root", d)

##############################################################################

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("Usage: jsonpath <input.json>")
        sys.exit(1)
    #
    fname = sys.argv[1]
    process(fname)
