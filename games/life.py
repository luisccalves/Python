# https://python-course.eu/tkinter/the-game-of-life-in-python.php

import sys
import tkinter
from dataclasses import dataclass
from random import random

__update__ = ''

if sys.version_info.major == 3 and sys.version_info.minor >= 9:
    listtype = list
else:
    from typing import List
    listtype = List


@dataclass
class Cell:
    value: int
    marked: bool = False
    
boardtype = listtype[listtype[Cell]]