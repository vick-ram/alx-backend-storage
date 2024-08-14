#!/usr/bin/env python3
"""web module"""
import redis
import requests
from typing import Callable
import functools

cache = redis.Redis()

def count_requests(method: Callable) -> Callable:
    """Decorator to count how many times a particular URL was accessed."""
    @functools.wraps(method)
    def wrapper(url: str, *args, **kwargs):
        cache.incr(f"count:{url}")
        return method(url, *args, **kwargs)

    return wrapper

def cache_page(method: Callable) -> Callable:
    """Decorator to cache the HTML content of a page with an expiration."""
    @functools.wraps(method)
    def wrapper(url: str, *args, **kwargs):
        cached_page = cache.get(f"cached:{url}")
        if cached_page:
            return cached_page.decode("utf-8")

        result = method(url, *args, **kwargs)

        cache.setex(f"cached:{url}", 10, result)
        return result

    return wrapper

@count_requests
@cache_page
def get_page(url: str) -> str:
    """Fetch the HTML content of a URL and cache it."""
    response = requests.get(url)
    return response.text

if __name__ == "__main__":
    url = "http://slowwly.robertomurray.co.uk/delay/5000/url/http://www.google.com"
    print(get_page(url))
    print(get_page(url))
    print(f"URL accessed {cache.get(f'count:{url}').decode('utf-8')} times")
