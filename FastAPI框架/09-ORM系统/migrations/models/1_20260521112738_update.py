from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE `course` ADD `addr` VARCHAR(32) NOT NULL COMMENT '教室';"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE `course` DROP COLUMN `addr`;"""


MODELS_STATE = (
    "eJztmV1P2zAUhv8KyhWT2JR+p7sr3dAYAyRg0yRAkZs4adTULo4zqFD++2wnqZ20yVLK2o"
    "B6U+jxsePz2D7nrfOsTbEN/eDT0AeB9vngWUNgCtk/GfvRgQZmM2nlBgpGvnC0Uo9RQAmw"
    "KLM5wA8gM9kwsIg3ox5GzIpC3+dGbDFHD7nSFCLvIYQmxS6kY0hYw+09M3vIhk8wSL/OJq"
    "bjQd/OTNOz+bOF3aTzmbCdInoiHPnTRqaF/XCKpPNsTscYLbw9RLnVhQgSQCEfnpKQT5/P"
    "LokyjSieqXSJp6j0saEDQp8q4VZkYGHE+bHZxOvg8qd8bDbavbbR6rYN5iJmsrD0ojg8GX"
    "vcURC4uNEi0Q4oiD0ERslN/F0iNxwDshpd6p+Dx6ach5eiKqOXGiQ+uWVK+Wl3Ya8FbfYJ"
    "Qe8u7LR1/n/f0bVqVKfgyfQhcumYfW01SxD+GlwNvw2uDlvND3xszLZ2vN8vkpamaIoivj"
    "WdiQKZG0bAmjwCYpuZFok/oKEN+aSWluA46XlydgV9IMJexp4czut4lK2uQOUdHKVbKLUm"
    "h0QAw01cRGy5adqc5i0AAVfMmj+bPylNVzgkAVyZyOKW8lQmffbJbJ/MtpDMjJEDWQID+q"
    "geyexI2Y3Atsk6VFP/3VPtdjp9xnME2vUgSSGwWCow1zrf2U7/Pufb3KqGrjcYYKgbFQG/"
    "QgJYqrNLfJfhnmACPRedwblgfMomBZC16uwnVeJGjvRW2BbVWWYm4HFRZXL7iYXOAoY0Pt"
    "OD6+Hgy1ctKpYuGxbtKsrnHKD5DeafFRdrA/nzwoqn8azS7bKl6jScu7Cv6/108Qyju/mC"
    "icDMnHJRwiRcEkJ74SEFi4OJWIgJnCuUk8VeLFPSGndLGumY4NAdq73ksCu3CbObeYURlc"
    "qyNIQVukyJrliYBYrTXpntldkWUrJ6zjt9uxXrs3roidnjiu1YDDVxrwNTizM19EY9OAYI"
    "r3GsE+/dK7F4a3ZaTm976kvFxm/81tOySo8d49tqZiyRrOmt6YZ6Nb2erR+/qrJU2Ro706"
    "SKjNpMkcpLpvcsSGWUeT2aEfdZRZrRnHlBmpWrmytSgbdckqa/9FZIUuVHYLEkVX5z7iVp"
    "3RLv+5SkybUW1I29JH2vkpSuJUlpXSSpujV7TmPr8vRFL+HiorLhO7iXl/y6XRj+1xdzA0"
    "g8a7yq2iYtpcUWSJ99rX1DtfYPJEFyeqpWBqXLjqtDdYqZmtDsdCoUBeZVWBVEW+5dHDsa"
    "a0BM3N8mwIauVwDIvAoBirbcnQVGNLlBzkL8fn15UXBpIbvkQP5ELMBb27Po0YHvBfS+nl"
    "hLKPKo+aSnQfDgq/AOzwe/81yHPy6PBQUcUJeIUcQAx+sV3tcvL9FfoM9k+Q=="
)
