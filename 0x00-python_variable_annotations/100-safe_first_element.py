#!/usr/bin/env python3
"""
Augmenting code with the correct duck-typed annotations
"""

from typing import Any, Sequence, Union, Optional


def safe_first_element(lst: sequence[Any]) -> Optional[Any]:
    """
    This returns the first element of a sequnence or None if sequence is empty
    """
    if lst:
        return lst[0]
    else:
        return None
