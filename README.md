# FastAPI-learning

从零开始学 Python → FastAPI → AI 应用开发，每日代码 + 笔记。

## 进度

| 天数 | 日期 | 内容 | 产出 |
|------|------|------|------|
| Day 1 | 5.11 | Python 基础语法 | `day1_basics.py` — 4 个函数：密码校验、FizzBuzz、打印三角、计算器 |
| Day 2 | 5.12 | Python 进阶 + API 调用 | `day2_class_api.py` — 列表/字典操作、Student 类、GitHub API 调用 |
| Day 3-4 | 5.13-14 | FastAPI + 数据库 CRUD | `day-3_fastapi/` — 9 个 RESTful 接口 + Pydantic 校验 + Tortoise ORM + MySQL |
| Day 5 | 5.15 | Git & GitHub | 本仓库上线 |
| Day 6 | 5.16 | LLM API 调用 | `day-6_llm_api.py` — DeepSeek API 单次对话 + 多轮对话 + FastAPI `/chat` 接口 |

## 项目结构

```
FastAPI-learning/
├── day1_basics.py              # Day 1：Python 基础手搓
├── day2_class_api.py           # Day 2：类与对象 + API 调用
├── day-6_llm_api.py            # Day 6：DeepSeek API 调用
├── day-3_fastapi/              # Day 3-4：FastAPI + 数据库 CRUD
│   ├── main.py                 #   FastAPI 路由和接口
│   ├── models.py               #   Tortoise ORM 数据模型
│   ├── settings.py             #   数据库连接配置
│   └── migrations/             #   Aerich 数据库迁移文件
├── python 学习/                 # Day 1-2 跟视频敲的 Python 练习
├── FastAPI框架/                 # Day 3-4 跟视频敲的 FastAPI 练习
└── README.md
```

## 技术栈

| 层级 | 技术 |
|------|------|
| 语言 | Python 3.13 |
| Web 框架 | FastAPI |
| 数据校验 | Pydantic |
| ORM | Tortoise ORM |
| 数据库 | MySQL |
| 迁移工具 | Aerich |
| LLM API | DeepSeek API + OpenAI 兼容格式 |
| 版本控制 | Git + GitHub |

## 本地运行

```bash
# 1. 克隆仓库
git clone https://github.com/YUANnnn11/FastAPI-learning.git
cd FastAPI-learning

# 2. 创建虚拟环境
python -m venv ai-env
ai-env\Scripts\activate   # Windows
# source ai-env/bin/activate  # macOS/Linux

# 3. 安装依赖
pip install fastapi uvicorn tortoise-orm aerich asyncmy pydantic requests python-dotenv

# 4. 配置环境变量
cd day-3_fastapi
cp .env.example .env
# 编辑 .env 文件，填入你的数据库密码和 API Key

# 5. 启动 FastAPI 服务
python main.py
# 访问 http://127.0.0.1:8000/docs 查看 Swagger 文档
```
