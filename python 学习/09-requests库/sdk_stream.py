# 底层协议是 Server-Sent Events (SSE)：服务器保持 HTTP 连接不断开，持续往里推送 data: {...}\n\n 这样的文本片段，直到发出 data: [DONE] 为止。
# 手写 SSE 解析比较麻烦，SDK 会帮你做好。
#
# 用 SDK 实现流式
# 把 stream=True 打开，返回值就从一个完整的响应对象变成一个可迭代的流：


# hello_stream.py
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com/v1",
)

stream = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "user", "content": "用三段话介绍一下 asyncio 的基本原理"},
    ],
    stream=True,
)

for chunk in stream:
    delta = chunk.choices[0].delta.content
    if delta:
        print(delta, end="", flush=True)
print()


# 注意两个容易踩的点：
#
# 每个 chunk 的内容在 choices[0].delta.content 里（不是 message.content），而且可能是 None（比如第一个 chunk 只包含 role 信息，没有文本）
# print 必须加 flush=True，否则 Python 的输出缓冲会让你看到的"流式"其实是攒了一批才一起输出，不流畅

