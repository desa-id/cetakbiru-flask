# Gunicorn configuration file.

import os
from dotenv import load_dotenv
from pathlib import Path
import multiprocessing

BASE_DIR = Path('.').resolve()
ENV_PATH = BASE_DIR.joinpath('.env')

load_dotenv(dotenv_path=ENV_PATH)

bind = os.getenv('APP_HOST') + ":" + os.getenv('APP_PORT')

backlog = 2048

# Set dynamic or static workers based on CPU
# workers = multiprocessing.cpu_count() * 2 + 1
workers = 1

worker_class = 'sync'
worker_connections = 1000
timeout = 30
keepalive = 2

daemon = False
reload = os.getenv('APP_DEBUG')
