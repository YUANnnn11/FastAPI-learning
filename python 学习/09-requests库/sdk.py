# 换用 openai SDK：代码瞬间清爽
# 原生 requests 的写法每次都要拼 header、处理 JSON、捕获异常，啰嗦。
# 官方有一个 openai Python SDK，虽然名字里有 OpenAI，但它接受自定义的 base_url，所以可以用来调任何兼容协议的服务：

# hello_sdk.py
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com/v1",
)

resp = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "system", "content": "你是一位简洁的 Python 老师。"},
        {"role": "user", "content": "什么是装饰器？"},
    ],
)

print(resp.choices[0].message.content)
print(f"消耗 Token：{resp.usage.total_tokens}")



# 和裸 requests 版本对比，减少了十几行样板代码，还多了类型提示、自动重试和参数校验。整个系列后面都用这种写法。想切换模型后端时，只改 base_url 和 api_key：
#
# # 换到 OpenAI 官方
# client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))  # base_url 默认就是 OpenAI
#
# # 换到本地 Ollama
# client = OpenAI(api_key="ollama", base_url="http://localhost:11434/v1")
#
# # 换到 Qwen
# client = OpenAI(
#     api_key=os.getenv("DASHSCOPE_API_KEY"),
#     base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
# )
# 代码主体完全不动。这就是 OpenAI 协议事实标准带来的便利。


