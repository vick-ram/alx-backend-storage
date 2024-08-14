#!/usr/bin/env python3
"""exercise module"""
import redis
import uuid
import functools
from typing import Union


def count_calls(method: callable) -> callable:
    """Decorator to count how many times a method is called."""
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)

    return wrapper


class Cache:
    """The redis cache"""

    def __init__(self) -> None:
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Store the data in Redis and return the key."""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key


    def get(self, key: str, fn: callable = None) -> Union[str, bytes, int, float, None]:
        """Get data from Redis and optionally process it with a function."""
        value = self._redis.get(key)
        if value is None:
            return None
        return fn(value) if fn else value


    def get_str(self, key: str) -> str:
        """Get a string from Redis."""
        return self.get(key, fn=lambda d: d.decoode("utf-8"))


    def get_int(self, key: str) -> int:
        """Get an integer from Redis."""
        return self.get(key, fn=int)
