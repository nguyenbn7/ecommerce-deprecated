import redis

r = redis.Redis(decode_responses=True)


async def get_redis_context():
    try:
        yield r
    finally:
        r.close()
