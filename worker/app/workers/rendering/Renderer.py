import redis

def renderWorkerThread(redis_connection_pool: redis.ConnectionPool):
    redis_client = redis.Redis(connection_pool=redis_connection_pool)
    while True:
        redis_client.blpop(['queued_render_tasks', 'once_errored_render_tasks'])