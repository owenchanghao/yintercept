from abc import ABC, abstractmethod

class ILog(ABC):
    @abstractmethod
    async def write(self, message: str):
        pass

    @abstractmethod
    async def stop(self, wait: bool):
        pass
