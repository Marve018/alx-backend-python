#!/usr/bin/env python3

""" Module that contains Asynchronous coroutine that takes in two arguments
  and returns a list of delayed float values.

  Args:
    n (int): The number of tasks to run concurrently.
    max_delay (int): The maximum delay for each task.

  Returns:
    List[float]: A list of delayed float values.
"""

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """ Asynchronous coroutine that takes in two arguments
          and returns a list of delayed float values.
    """

    delayed_tasks = []  # init empty list to store delayed tasks
    tasks = [wait_random(max_delay) for _ in range(n)]
    completed = asyncio.as_completed(tasks)
    for task in completed:
        result = await task
        delayed_tasks.append(result)
    return delayed_tasks  # list of delayed tasks sorted in ascending order
