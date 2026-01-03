from flask import Flask
import redis
import os
import random

app = Flask(__name__)

# Connect to Redis (This will fail initially - that's the plan!)
redis_host = os.environ.get('REDIS_HOST', 'localhost')
cache = redis.Redis(host=redis_host, port=6379)

@app.route('/')
def hello():
    # Simulation: 10% chance the app "crashes"
    if random.random() < 0.1:
        return "Internal Server Error - Simulating a Crash!", 500
    
    try:
        count = cache.incr('hits')
        return f'Hello! This site has been visited {count} times.\n'
    except redis.exceptions.ConnectionError:
        return 'CRITICAL ERROR: Redis is unreachable! (Is the database running?)', 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)