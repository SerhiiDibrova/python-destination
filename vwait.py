import asyncio

class VWait:
    def __init__(self, condition):
        self.condition = condition

    async def wait(self):
        loop = asyncio.get_event_loop()
        future = loop.create_future()
        self.condition.register(future.set_result)
        await future
        self.condition.unregister(future.set_result)