import os
from dotenv import load_dotenv

load_dotenv()

TORTOISE_ORM = {
    'connections': {
        'default': {
            'engine': 'tortoise.backends.mysql',
            'credentials': {
                'host': os.getenv('DB_HOST', '127.0.0.1'),
                'port': os.getenv('DB_PORT', '3306'),
                'user': os.getenv('DB_USER', 'root'),
                'password': os.getenv('DB_PASSWORD'),
                'database': os.getenv('DB_NAME', 'ai_demo'),
                'minsize': 1,
                'maxsize': 5,
                'charset': 'utf8mb4',
                'echo': True,
            },
        },
    },
    'apps': {
        'models': {
            'models': ['models', 'aerich.models'],
            'default_connection': 'default',
        },
    },
    'use_tz': False,
    'timezone': 'Asia/Shanghai',
}
