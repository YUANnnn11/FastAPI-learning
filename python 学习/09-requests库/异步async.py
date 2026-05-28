# 异步版本：应对高并发
# 以上都是同步代码，单个请求没问题。
# 但如果你要同时发起几十个请求（比如批量处理文档、并行调用多个模型比较结果），同步就扛不住了——每个请求要几秒，串行跑完需要几分钟。
# 这时候用 asyncio + AsyncOpenAI：

# hello_async.py
import asyncio
import os
from openai import AsyncOpenAI
from dotenv import load_dotenv

load_dotenv()

client = AsyncOpenAI(
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com/v1",
)

async def ask(question: str) -> str:
    resp = await client.chat.completions.create(
        model="deepseek-chat",
        messages=[{"role": "user", "content": question}],
    )
    return resp.choices[0].message.content

async def main():
    questions = [
        "用一句话解释什么是 GIL",
        "用一句话解释什么是事件循环",
        "用一句话解释什么是协程",
    ]
    results = await asyncio.gather(*[ask(q) for q in questions])
    for q, r in zip(questions, results):
        print(f"Q: {q}\nA: {r}\n")

asyncio.run(main())


# 三个请求并行发出，总耗时约等于最慢那一个，而不是三个相加。实际工程中处理百万级文档都靠这套模式。

