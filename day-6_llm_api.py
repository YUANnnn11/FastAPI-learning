# 任务 1：最简单的对话
import os
import requests
from dotenv import load_dotenv

load_dotenv()   # 从 .env 读 API Key

def chat(prompt):
    """发送消息给 DeepSeek，返回 AI 的回复文本"""
    response = requests.post(
        f"{os.getenv('DEEPSEEK_BASE_URL')}/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {os.getenv('DEEPSEEK_API_KEY')}",
            "Content-Type": "application/json"
        },
        json={
            "model": "deepseek-chat",
            "messages": [{"role": "user", "content": prompt}],
            "temperature": 0.7
        }
    )
    data = response.json()
    return data["choices"][0]["message"]["content"]

# 测试
print(chat("用一句话解释什么是 RAG"))

# 任务 2：多轮对话
# 给 chat 函数加上 messages 参数，让它支持上下文
# 做一个命令行对话循环：用户输入 → AI 回复 → 继续等待输入 → 输入 quit 退出

def chat_with_history(messages):
    """发送消息给 DeepSeek，返回 AI 的回复文本"""
    response = requests.post(
        f"{os.getenv('DEEPSEEK_BASE_URL')}/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {os.getenv('DEEPSEEK_API_KEY')}",
            "Content-Type": "application/json"
        },
        json={
            "model": "deepseek-chat",
            "messages": messages,
            "temperature": 0.7
        }
    )

    data = response.json()
    return data["choices"][0]["message"]["content"]

messages = []
while True:
    user_input = input("你：")
    if user_input == "quit":
        break
    messages.append({"role": "user", "content": user_input})
    reply = chat_with_history(messages)
    messages.append({"role": "assistant", "content": reply})
    print(f"AI：{reply}")

# 任务 3（选做）：把 chat 包装成 FastAPI 接口
# POST /chat  接收 {"message": "..."}  返回 {"reply": "..."}

from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel

app = FastAPI()

class ChatRequest(BaseModel):
    message: str

@app.post("/chat")
def chat(request: ChatRequest):
    response = requests.post(
        f"{os.getenv('DEEPSEEK_BASE_URL')}/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {os.getenv('DEEPSEEK_API_KEY')}",
            "Content-Type": "application/json"
        },
        json={
            "model": "deepseek-chat",
            "messages": [{"role": "user", "content": request.message}],
            "temperature": 0.7
        }
    )
    data = response.json()
    return {"reply": data["choices"][0]["message"]["content"]}

if __name__ == "__main__":
    uvicorn.run("day-6_llm_api:app", host="127.0.0.1", port=8080)
