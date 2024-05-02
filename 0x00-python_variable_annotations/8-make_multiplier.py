#!/usr/bin/env python3
"""
This module contains function make_multiplier that takes float multiplier
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    This returns a function that multiplies a float by multiplier
    """
    def multipler_func(n: float) -> float:
        return n * multiplier
    return multiplier_func
