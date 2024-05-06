#!/usr/bin/env python3
'''
This module contains the coroutine wait_n that takes in an integer n
and an integer max_delay and returns the list of all the delays
'''
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> list[float]:
    """
    Takes in an integer n and an integer max_delay
    and returns a list of floats of all the delays
    """
    tasks = [asyncio.create_task(wait_random(max_delay)) for i in range(n)]
    return await asyncio.gather(*tasks)
