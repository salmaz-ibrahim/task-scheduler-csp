import json
import os
import urllib.error
import urllib.request
from datetime import datetime
from zoneinfo import ZoneInfo


OLLAMA_URL = os.getenv("OLLAMA_URL", "http://localhost:11434/api/chat")
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "llama3.2")


def _extract_json(text):
    cleaned = (
        text
        .replace("```json", "")
        .replace("```", "")
        .strip()
    )

    start = cleaned.find("{")
    end = cleaned.rfind("}")

    if start == -1 or end == -1:
        raise ValueError("Ollama did not return JSON.")

    return json.loads(cleaned[start:end + 1])


def _call_ollama(prompt):
    payload = {
        "model": OLLAMA_MODEL,
        "stream": False,
        "messages": [
            {
                "role": "system",
                "content": (
                    "You are a scheduling assistant. Return only valid JSON. "
                    "Do not include markdown, comments, or extra text."
                )
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        "options": {
            "temperature": 0.1
        }
    }

    request = urllib.request.Request(
        OLLAMA_URL,
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"},
        method="POST"
    )

    try:
        with urllib.request.urlopen(request, timeout=300) as response:
            result = json.loads(response.read().decode("utf-8"))
    except urllib.error.URLError as error:
        raise ConnectionError(
            "Could not reach Ollama. Make sure Ollama is running locally."
        ) from error

    return result["message"]["content"]


def create_schedule_with_ollama(user_input):
    date = datetime.now(ZoneInfo("Africa/Cairo")).strftime("%Y-%m-%d")

    prompt = """
    You are an extraction assistant.

    Return only valid JSON.
    Do not include markdown, comments, explanations, or extra text.

    Extract tasks from the user's request.

    For each task, return:
    - name
    - duration_hours
    - priority

    Rules:
    - Infer duration if the user mentions it.
    - If duration is missing, use 1 hour.
    - Priority must be one of: high, medium, low.
    - If the user expresses urgency (e.g. "important", "must", "need to"), use high priority.
    - Otherwise, use medium priority.
    - Preserve the user's intent.
    - Do NOT schedule tasks.
    - Do NOT choose dates or times.
    - Do NOT create calendar events.

    Return JSON in exactly this format:
    {{
    "tasks": [
        {{
        "name": "Study machine learning",
        "duration_hours": 1,
        "priority": "high"
        }}
    ]
    }}
    User request:
    USER_INPUT
    """
    prompt = prompt.replace("USER_INPUT", user_input)
    response_text = _call_ollama(prompt)
    task_payload = _extract_json(response_text)
    return _validate_task_payload(task_payload)



def _validate_task_payload(task_payload):

    if not isinstance(task_payload, dict):
        raise ValueError("Ollama response must be a JSON object.")

    tasks = task_payload.get("tasks")

    if not isinstance(tasks, list):
        raise ValueError("Ollama response must contain a tasks list.")

    for task in tasks:

        required = {
            "name",
            "duration_hours",
            "priority"
        }

        if not required.issubset(task):
            raise ValueError(
                f"Task is missing fields: {task}"
            )

        task["name"] = str(task["name"]).strip()

        if task["priority"] not in {
            "high",
            "medium",
            "low"
        }:
            raise ValueError(
                f"Invalid priority: {task['priority']}"
            )

        if task["duration_hours"] <= 0:
            raise ValueError(
                f"Invalid duration for {task['name']}"
            )

    return {
        "tasks": tasks
    }
