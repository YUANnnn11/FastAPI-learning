# 先不使用任何 SDK，用 requests 直接打接口，这样协议最透明：

# hello_raw.py
import os
import requests
from dotenv import load_dotenv

load_dotenv()

resp = requests.post(
    "https://api.deepseek.com/v1/chat/completions",
    headers={
        "Authorization": f"Bearer {os.getenv('DEEPSEEK_API_KEY')}",
        "Content-Type": "application/json",
    },
    json={
        "model": "deepseek-chat",
        "messages": [
            {"role": "user", "content": "用一句话解释什么是闭包"}
        ],
    },
    timeout=30,
)

data = resp.json()
# print(data)
print(data["choices"][0]["message"]["content"])


# URL：https://api.deepseek.com/v1/chat/completions，是 OpenAI /v1/chat/completions 的镜像路径
# 请求头 Authorization: Bearer <key>，标准 OAuth2 风格
# 请求体有两个关键字段：model 指定要调用哪个模型，messages 是对话内容
# 响应结构固定：choices[0].message.content 是模型的回答，此外还有 usage 字段记录消耗了多少 Token
# 这就是所有 LLM 调用的骨架。后面的所有"高级特性"都是在这个骨架上加字段。

