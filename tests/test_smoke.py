import importlib
import sys
from pathlib import Path

# Add project root to path so imports resolve
sys.path.insert(0, str(Path(__file__).parent.parent))


def test_server_importable():
    mod = importlib.import_module("mcp_server")
    assert hasattr(mod, "mcp")
    assert hasattr(mod, "echo")
    assert hasattr(mod, "write_file")


def test_client_importable():
    mod = importlib.import_module("mcp_client")
    assert hasattr(mod, "MCPClient")
