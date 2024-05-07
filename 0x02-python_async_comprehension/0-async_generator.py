#!/usr/bin/env python3
"""
This module defines an asynchronous generator called async_generator that
takes no arguments
"""

import asyncio
import random


async def async_generator() -> asyncio.StreamReader:
    """
    An asynchronous generator that yields random numbers between 0 and 10
    with a 1-second delay between each yield.

    Loops 10 times.

    Returns:
        asyncio.StreamReader: An asynchronous generator object.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
