#!/usr/bin/env python3
"""This module contains a coroutine called measure_runtime that will execute
4 coroutines concurrently using asyncio.gather and measure the total runtime"""

import asyncio
from time import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """The coroutine will execute async_comprehension four times in parallel
    and measure the total runtime."""
    start = time()
    await asyncio.gather(*[async_comprehension() for _ in range(4)])
    end = time()
    return (end - start)
