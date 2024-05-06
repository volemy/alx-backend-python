#!/usr/bin/env python3
"""
This module provides functionality to measure the runtime of the asynchronous
wait_n function.
"""

import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    This function measures the total execution time of wait_n divided
    by n to find the average time
    """
    start_time = time.time()  # Record the start time
    asyncio.run(wait_n(n, max_delay))  # Execute the asynchronous function
    end_time = time.time()  # Record the end time
    total_time = end_time - start_time  # Calculate total time
    return total_time / n  # Return the average time per operation

