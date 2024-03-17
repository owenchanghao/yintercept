import pytest
import asyncio
from file_logger import FileLogger

@pytest.mark.asyncio
async def test_log_write():
    logger = FileLogger()
    await logger.write("Test log entry")
    await logger.stop(wait=True)
    # Further implementation required to verify the log entry is written to the file.

@pytest.mark.asyncio
async def test_new_file_creation_at_midnight():
    # This would require mocking or simulating the date change.
    pass

@pytest.mark.asyncio
async def test_stop_behaviors():
    # Test both immediate stop and waiting for log queue to be emptied.
    pass
