#!/usr/bin/env python3
"""
This module contains the coroutine wait_n that takes in an integer n
and an integer max_delay and returns the list of all the delays
"""
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Generates a list of delays of length `count` with a maximum
    value of `max_delay`
    """
    delays = await asyncio.gather(*(
        wait_random(max_delay) for _ in range(n)))
    return sorted(delays)
