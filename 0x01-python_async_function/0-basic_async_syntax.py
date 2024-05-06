#!/usr/bin/env python3
"""
This module defines an asynchronous coroutine that
waits for a random amount of time.
"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    This function asynchronously waits for a random time
    between 0 and max_delay seconds.
    """
    delay: float = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay

