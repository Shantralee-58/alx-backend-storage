#!/usr/bin/env python3
"""
Web Cache and Tracker
"""
import requests
import redis
import time
import uuid

r = redis.Redis()

def get_page(url: str) -> str:
    count_key = f"count:{url}"
    r.incr(count_key)
    cache_key = f"cache:{url}"
    cached_content = r.get(cache_key)
    if cached_content:
        return cached_content.decode('utf-8')
    response = requests.get(url)
    content = response.text
    r.setex(cache_key, 10, content)
    return content
