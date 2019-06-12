from bgtask import task, update_config

update_config(dict(
    REDIS_HOST='127.0.0.1',
    REDIS_PORT='6379',
    TASK_QUEUE_KEY="mytask",
    TASK_WORKER=2
))


@task()
def do_add(x, y):
    print "sum of ", x, "+", y, "=", x+y
