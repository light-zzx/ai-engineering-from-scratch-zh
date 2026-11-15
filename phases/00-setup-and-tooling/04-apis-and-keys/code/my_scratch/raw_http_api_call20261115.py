import os
import urllib.request
import json

url = "https://api.deepseek.com/anthropic/v1/messages"

headers = {
    "Content-Type": "application/json",
    "x-api-key": os.environ["DEEPSEEK_API_KEY"],
}

body = json.dumps({
    "model": os.environ.get("LLM_MODEL", "deepseek-flash"),
    "max_tokens": 256,
    "messages": [{"role": "user", "content": "请用一句话描述什么是神经网络"}],
    "thinking": {"type": "disabled"},
}).encode()

req = urllib.request.Request(url, data=body, headers=headers, method="POST")
with urllib.request.urlopen(req) as resp:
    result = json.loads(resp.read())
    print(result["content"][0]["text"])
