#!/usr/bin/env python3
"""This module contains a coroutine called async_comprehension that takes no
parameter and returns an async comprehension."""

import asyncio
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """The coroutine will collect 10 random numbers using an async
    comprehensing over the async_generator function."""
    return [num async for num in async_generator()]
