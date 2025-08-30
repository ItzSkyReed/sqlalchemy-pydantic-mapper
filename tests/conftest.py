import sys
from pathlib import Path

import pytest


sys.path.append(str(Path(__file__).resolve().parent.parent))

from src.sqlalchemy_pydantic_mapper import ObjectMapper

pytestmark = pytest.mark.anyio


@pytest.fixture(scope="session", autouse=True)
def anyio_backend():
    return "asyncio"

@pytest.fixture
async def object_mapper():
    ObjectMapper.clear()
    return ObjectMapper
