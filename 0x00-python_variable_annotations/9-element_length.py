#!/usr/bin/env python3
"""
This module adds annotations to below function
"""

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    This function returns a list of tuples where each tuple contains a 
    sequence and an integer
    """
    return [(i, len(i)) for i in lst]
