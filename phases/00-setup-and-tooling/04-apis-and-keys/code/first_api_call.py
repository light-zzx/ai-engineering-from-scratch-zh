import os
import json
import urllib.request

# MODEL = os.environ.get("LLM_MODEL", "claude-sonnet-5")
MODEL = "deepseek-flash"  # 使用deepseek模型代理原来的claude


def call_with_sdk():
    try:
        import anthropic
    except ImportError:
        print("Install the SDK: pip install anthropic")
        return

    # client = anthropic.Anthropic()
    client = anthropic.Anthropic(
    api_key=os.environ.get("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com/anthropic"
    )  # 设置api_key和base_url就可以替换原始厂商了

    response = client.messages.create(
        model=MODEL,
        max_tokens=256,
        messages=[{"role": "user", "content": "请用一句话描述什么是神经网络"}],
        thinking={"type": "disabled"}
    )

    print(f"SDK response: {response.content[0].text}")
    print(f"Tokens used: {response.usage.input_tokens} in, {response.usage.output_tokens} out")


def call_raw_http():
    # api_key = os.environ.get("ANTHROPIC_API_KEY")
    api_key = os.environ.get("DEEPSEEK_API_KEY")
    if not api_key:
        print("Set ANTHROPIC_API_KEY environment variable first")
        return

    # url = "https://api.anthropic.com/v1/messages"
    url = "https://api.deepseek.com/anthropic/v1/messages"

    headers = {
        "Content-Type": "application/json",
        "x-api-key": api_key,
        # "anthropic-version": "2023-06-01",
    }
    # body = json.dumps({
    #     "model": MODEL,
    #     "max_tokens": 256,
    #     "messages": [{"role": "user", "content": "What is a neural network in one sentence?"}],
    # }).encode()

    body = json.dumps({
    "model": os.environ.get("LLM_MODEL", "deepseek-flash"),
    "max_tokens": 256,
    "messages": [{"role": "user", "content": "请用一句话描述什么是神经网络"}],
    "thinking": {"type": "disabled"},
    }).encode()

    req = urllib.request.Request(url, data=body, headers=headers, method="POST")
    with urllib.request.urlopen(req) as resp:
        result = json.loads(resp.read())
        print(f"Raw HTTP response: {result['content'][0]['text']}")
        print(f"Tokens used: {result['usage']['input_tokens']} in, {result['usage']['output_tokens']} out")


if __name__ == "__main__":
    print("=== API Calls ===\n")
    print("1. Using the SDK:")
    call_with_sdk()
    print("\n2. Using raw HTTP:")
    call_raw_http()
