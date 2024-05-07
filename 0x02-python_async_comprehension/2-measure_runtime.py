#!/usr/bin/env python3
"""
This module imports async_comprehension from previos file
"""

import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    This method measures the total runtime of executing async_comprehension
    four times in parallel and returns the total runtime in seconds.
    """
    start_time = time.time()
    tasks = [async_comprehension() for _ in range(4)]
    await asyncio.gather(*tasks)
    end_time = time.time()
    return end_time - start_time
