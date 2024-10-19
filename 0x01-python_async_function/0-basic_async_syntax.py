#!/usr/bin/env python3

import asyncio
import random

async def wait_random(max_delay: int = 10) -> float:
    delay = random.uniform(0, max_delay)
    
    await asyncio.sleep(delay)
    
    return delay


result = asyncio.run(wait_random(10))
print(f"Waited for {result} seconds.")
