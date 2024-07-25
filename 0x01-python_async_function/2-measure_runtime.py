#!/usr/bin/env python3

""" Module that contains a function that takes 2 args and measures
the total execution time for wait_n(n, max_delay),
and returns total_time / n. Function should return a float.
"""

import time
from asyncio import run

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """ Function that measures the total execution time for
    wait_n(n, max_delay), and returns total_time / n.
    """
    start_time = time.time()
    run(wait_n(n, max_delay))
    end_time = time.time()
    total_time = end_time - start_time

    return total_time / n
