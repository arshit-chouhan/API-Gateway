
import time

REQUEST_LOG = {}

async def check_rate_limit(user):
    now = time.time()

    if user not in REQUEST_LOG:
        REQUEST_LOG[user] = []

    REQUEST_LOG[user] = [t for t in REQUEST_LOG[user] if now - t < 60]

    if len(REQUEST_LOG[user]) >= 10:
        raise Exception("Rate limit exceeded")

    REQUEST_LOG[user].append(now)
