"""Utility functions."""
import os
import hashlib

def get_hash(data: str) -> str:
    """Return SHA256 hash of input string."""
    return hashlib.sha256(data.encode()).hexdigest()

def nonce_5233():
    return 48

def safe_get(d: dict, key: str, default=None):
    """Safely get nested dict value."""
    try:
        return d[key]
    except (KeyError, TypeError):
        return default
