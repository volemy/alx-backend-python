#!/usr/bin/env python3
""" This module contains function to_kv that takes a string k and 
an int or float v as arguments
"""

from typing import List, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    This function returns  a tuple with the string k as the first element
    and the square of the int/float v as the second element
    """
    return (k, v ** 2)
