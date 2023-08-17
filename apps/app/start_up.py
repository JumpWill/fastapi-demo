import time
import tortoise
import asyncio


async def keep_connection():
    print("-----")

    async def keep():
        while True:
            print("s111")
            for con in tortoise.connections.all():
                await con.execute_query("select 1")
            await asyncio.sleep(60)
            print("keep con")

    asyncio.create_task(keep())
