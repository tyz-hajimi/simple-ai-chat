#!/usr/bin/env python3
"""命令行 AI 对话：调用 OpenAI 兼容的 Chat Completions 接口（零第三方依赖）。"""

from __future__ import annotations

import json
import os
import sys
import urllib.error
import urllib.request


def chat_request(
    base_url: str,
    api_key: str,
    model: str,
    messages: list[dict[str, str]],
    temperature: float,
) -> str:
    url = f"{base_url.rstrip('/')}/chat/completions"
    body = {
        "model": model,
        "messages": messages,
        "temperature": temperature,
    }
    req = urllib.request.Request(
        url,
        data=json.dumps(body).encode("utf-8"),
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}",
        },
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=120) as resp:
        data = json.loads(resp.read().decode("utf-8"))
    return data["choices"][0]["message"]["content"]


def main() -> None:
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        print("请先设置环境变量 OPENAI_API_KEY。", file=sys.stderr)
        sys.exit(1)

    base_url = os.environ.get("OPENAI_BASE_URL", "https://api.openai.com/v1")
    model = os.environ.get("OPENAI_MODEL", "gpt-4o-mini")
    temp = float(os.environ.get("OPENAI_TEMPERATURE", "0.7"))
    system = os.environ.get("OPENAI_SYSTEM", "You are a helpful assistant.")

    messages: list[dict[str, str]] = []
    if system.strip():
        messages.append({"role": "system", "content": system})

    print("简易 AI 对话 — 输入 exit / quit 退出，/reset 清空上下文\n")

    while True:
        try:
            user_input = input("你: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\n再见。")
            break

        if not user_input:
            continue
        low = user_input.lower()
        if low in ("exit", "quit", "q"):
            print("再见。")
            break
        if user_input == "/reset":
            messages = [{"role": "system", "content": system}] if system.strip() else []
            print("（已清空对话上下文）\n")
            continue

        messages.append({"role": "user", "content": user_input})

        try:
            reply = chat_request(base_url, api_key, model, messages, temp)
        except urllib.error.HTTPError as e:
            err_body = e.read().decode("utf-8", errors="replace")
            print(f"HTTP {e.code}: {err_body}", file=sys.stderr)
            messages.pop()
            continue
        except urllib.error.URLError as e:
            print(f"网络错误: {e.reason}", file=sys.stderr)
            messages.pop()
            continue
        except (KeyError, IndexError, TypeError) as e:
            print(f"解析响应失败: {e}", file=sys.stderr)
            messages.pop()
            continue

        messages.append({"role": "assistant", "content": reply})
        print(f"AI: {reply}\n")


if __name__ == "__main__":
    main()
