import sys
from pathlib import Path

import pytest

sys.path.append(str(Path(__file__).resolve().parent.parent))


pytestmark = pytest.mark.anyio


@pytest.fixture(scope="session", autouse=True)
def anyio_backend():
    return "asyncio"
