#!/usr/bin/env python3
"""
This module contains the coroutine `task_wait_n` that takes in an integer n
and an integer max_delay and returns the list of all the delays
"""
import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Generates a list of delays of length `count` with a maximum
    value of `max_delay`
    """
    delays = await asyncio.gather(
        *(task_wait_random(max_delay) for _ in range(n))
        )
    return sorted(delays)
