import asyncio
import aiofiles
from datetime import datetime
from ilog_interface import ILog

class FileLogger(ILog):
    def __init__(self):
        self.current_date = datetime.now().date()
        self.file_name = self._generate_file_name()
        self.log_queue = asyncio.Queue()
        self.stop_requested = False
        self.wait_for_logs = True
        asyncio.create_task(self._process_log_queue())

    def _generate_file_name(self):
        return f"log_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.txt"

    async def write(self, message: str):
        await self.log_queue.put(message)

    async def _process_log_queue(self):
        while not self.stop_requested or (self.wait_for_logs and not self.log_queue.empty()):
            if datetime.now().date() != self.current_date:
                self.file_name = self._generate_file_name()
                self.current_date = datetime.now().date()
            message = await self.log_queue.get()
            async with aiofiles.open(self.file_name, 'a') as log_file:
                await log_file.write(f"{message}\n")
            self.log_queue.task_done()

    async def stop(self, wait: bool):
        self.stop_requested = True
        self.wait_for_logs = wait
