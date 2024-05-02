#!/usr/bin/env python3
"""
Augmenting code with the correct duck-typed annotations
"""

from typing import Sequence, Any, Union, Type


def safe_first_element(lst: sequence[Any]) -> Union[Any, Type[None]]:
    """
    This returns the first element of a sequnence or None if sequence is empty
    """
    if lst:
        return lst[0]
    else:
        return None
