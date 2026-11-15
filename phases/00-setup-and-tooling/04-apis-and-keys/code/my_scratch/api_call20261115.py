import os
import anthropic

client = anthropic.Anthropic(
    api_key=os.environ.get("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com/anthropic"
)  # 设置api_key和base_url就可以替换原始厂商了

MODEL = "deepseek-flash"  # 使用deepseek模型代理原来的claude

response = client.messages.create(
    model=MODEL,
    max_tokens=256,
    messages=[{"role": "user", "content": "请用一句话描述什么是神经网络"}],
    thinking={"type": "disabled"}
)

print(response.content[0].text)  # 模型生成的是列表包裹的json格式，访问第0个元素的text字段就是模型的回答
