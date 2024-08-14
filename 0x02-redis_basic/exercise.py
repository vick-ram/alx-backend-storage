#!/usr/bin/env python3
"""exercise module"""
import redis
import uuid
import functools
from typing import Union


class Cache:
    """The redis cache"""
    def __init__(self) -> None:
        self._redis = redis.Redis()
        self._redis.flushdb()


    def store(self, data: Union[str, bytes, int, float]) -> str:
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key


    def get(self, key: str, fn: callable = None) -> Union[str, bytes, int, float, None]:
        value = self._redis.get(key)
        if value is None:
            return None
        return fn(value) if fn else value


    def get_str(self, key: str) -> str:
        return self.get(key, fn=lambda d: d.decoode("utf-8"))


    def get_int(self, key: str) -> int:
        return self.get(key, fn=int)


    def count_calls(self, func):
        @functools.wraps(func)
        def wrapper(self, *args, **kwargs):
            key = func.__qualname__
            self._redis.incr(key)
            return func(self, *args, **kwargs)
        return wrapper


    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
