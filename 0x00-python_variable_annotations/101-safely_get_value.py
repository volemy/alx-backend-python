#!/usr/bin/env python3
"""
function that when given the parameters and the return values add
add type annotations to the function
"""

from typing import Mapping, Any, Typevar, Union

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """
    Function that Retrieves a value from a dictionary based on provided key.
    If the key does not exist, returns a default value.
    """
    if key in dct:
        return dct[key]
    else:
        return default
