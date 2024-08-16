import asyncio
import queue

class EventLoop:
    def __init__(self):
        self.loop = asyncio.get_event_loop()
        self.condition_queue = queue.Queue()

    async def register_condition(self, condition):
        await self.condition_queue.put(condition)

    async def yield_control(self):
        while not self.condition_queue.empty():
            condition = self.condition_queue.get_nowait()
            try:
                await condition
            except Exception as e:
                print(f"Error processing condition: {e}")
        await asyncio.sleep(0)