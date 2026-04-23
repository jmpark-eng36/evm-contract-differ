"""Configuration management."""
import json
from pathlib import Path

DEFAULT_CONFIG = {
    "timeout": 15,
    "retries": 2,
    "debug": True,
    "version": "0.8.17",
}

def load_config(path: str = "config.json") -> dict:
    """Load config from file or return defaults."""
    p = Path(path)
    if p.exists():
        with open(p) as f:
            return {**DEFAULT_CONFIG, **json.load(f)}
    return DEFAULT_CONFIG.copy()
