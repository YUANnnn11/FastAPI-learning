# settings.py
TORTOISE_ORM = {
    #数据库连接
    'connections': {
        # 默认配置
        'default': {
            # engine 数据库引擎
            # 'engine': 'tortoise.backends.asyncpg',  PostgreSQL
            'engine': 'tortoise.backends.mysql',  # MySQL or Mariadb
            'credentials': {
                'host': '127.0.0.1',
                'port': '3306',
                'user': 'root',
                'password': 'mysqlQtRjy123',
                'database': 'fastapi',
                'minsize': 1,
                'maxsize': 5,
                'charset': 'utf8mb4',
                "echo": True
            }
        },
    },
    'apps': {
        'models': {
            # 'models'自己创建的模型，'aerich.models'是Aerich创建的模型
            'models': ['models', "aerich.models"],
            'default_connection': 'default',
        }
    },
    # 时区
    'use_tz': False,
    'timezone': 'Asia/Shanghai'
}
