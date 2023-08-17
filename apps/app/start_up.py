import tortoise
import asyncio
from apps.common.log import logger


async def keep_connection():
    async def keep():
        while True:
            logger.info("start keeping db")
            for con in tortoise.connections.all():
                await con.execute_query("select 1")
            logger.info("keep db ok")
            await asyncio.sleep(60)

    asyncio.create_task(keep())
