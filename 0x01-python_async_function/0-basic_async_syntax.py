#!/usr/bin/env python3
"""Asynchronous coroutine that takes in an integer argument
 and returns a float."""
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """Takes an integer max_delay and returns a random delay in float"""
    return random.uniform(0, max_delay)
