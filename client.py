import random
import time
import logging

import redis
import dill

NUM_TASKS = 100

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def do_something(arg1, arg2):
    """ dummy function waits a random amount of time"""

    logger.info("performing task with args1=%s and arg2=%s", arg1, arg2)
    time.sleep(random.uniform(0.0, 1))

def main_client():

    # Configure our redis client
    r = redis.Redis(
            host='localhost',
            port=6379
    )

    # Generate N tasks

    logger.info("Generating %i tasks", NUM_TASKS)

    for i in range(NUM_TASKS):

        # Generate two random arguments
        a1 = random.randrange(0, 100)
        a2 = random.randrange(0, 100)

        #serialize the task and it's arguments
        data = dill.dumps((do_something, [a1, a2]))

        # Store it in the message broker
        r.rpush('tasks', data)

if __name__ == '__main__':
    main_client()
