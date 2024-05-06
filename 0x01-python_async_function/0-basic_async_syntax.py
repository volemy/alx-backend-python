#!/usr/bin/env python3
"""
This module contains a a wait_random function
"""

import asyncio
import random


async def wait_random(max_delay: float = 10) -> float:
    """
    An asynchronous coroutine that waits for a random delay between 0 and max_delay
    (included and float value) seconds and eventually returns it.

    Args:
        max_delay (float, optional): Maximum delay. Defaults to 10.

    Returns:
        float: The random delay.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
