#!/usr/bin/env python3
"""This module contains a coroutine called async_generator that takes no
parameter and returns an async iterator."""

import asyncio
import random
from typing import AsyncIterator


async def async_generator() -> AsyncIterator[float]:
    """The coroutine will loop 10 times, each time asynchronously
    wait 1 second, then yield a random number between 0 and 10."""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
