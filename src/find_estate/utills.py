import random

import time

import asyncio

async def external_server() -> bool:
    # await asyncio.sleep(random.randint(1, 60))
    return random.choice([True, False])
 