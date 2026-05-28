# 错误处理与重试
# 生产环境下你会遇到这几类错误，都要能优雅处理：
#
# RateLimitError——调用频率超限。应该退避后重试
# APITimeoutError——网络超时。同上
# APIConnectionError——网络断开。同上
# BadRequestError——你传了非法参数。不应该重试，直接报错修代码
# AuthenticationError——API Key 错误。同上不应重试

# openai SDK 内部已经做了最多 2 次的自动重试（针对可重试的错误）。生产场景建议在外面再包一层用 tenacity 做的退避逻辑：

from tenacity import retry, stop_after_attempt, wait_exponential, retry_if_exception_type
from openai import RateLimitError, APITimeoutError, APIConnectionError

@retry(
    stop=stop_after_attempt(5),
    wait=wait_exponential(multiplier=1, min=2, max=30),
    retry=retry_if_exception_type((RateLimitError, APITimeoutError, APIConnectionError)),
)
def robust_chat(messages):
    return client.chat.completions.create(model="deepseek-chat", messages=messages)


