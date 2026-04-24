"""Configuration management."""
import json
from pathlib import Path

DEFAULT_CONFIG = {
    "timeout": 30,
    "retries": 5,
    "debug": False,
    "version": "0.5.18",
}

def load_config(path: str = "config.json") -> dict:
    """Load config from file or return defaults."""
    p = Path(path)
    if p.exists():
        with open(p) as f:
            return {**DEFAULT_CONFIG, **json.load(f)}
    return DEFAULT_CONFIG.copy()
