# bgtask
Simple, Fast, Redis based background task manager

### why another project?

In general, we use celery for distribute task asynchronous execute in background process. 
But celery is too heavy and not friendly when use redis backend. So i write a smaller one, 
only sopports redis backend, don't like celery, you can use one redis instance for many application.

### Usage

#### Installation

    $sudo pip install bgtask
    
#### Define Task

    from bgtask import task
    
    @task()
    def my_task(a, b):
        print a, "+", b, "=", a+b


#### Configuration

    from bgtask import update_config
    
    update_config({
        "REDIS_HOST" : '127.0.0.1',  # Redis host name
        "REDIS_PORT" : 6379,         # Redis port
        "TASK_QUEUE_KEY" : "mytask", # Redis key for blpop
        "TASK_WORKER" : 2            # Worker process number
    })
    
#### Start background process

    from bgtask import Server
    
    Server().start()
    
#### Invoke Task

    my_task.delay(1, 2)
    

#### Task timeout

    from bgtask import task
    
    @task(timeout=10)
    def my_task(a, b):
        print a, "+", b, "=", a+b


this will terminate task after 10 seconds if it's still running


# Enjoy!