#!/usr/bin/env python3
"""This module contains the task_wait_random function"""

import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Takes an integer max_delay and returns a random delay in float"""
    return asyncio.create_task(wait_random(max_delay))
