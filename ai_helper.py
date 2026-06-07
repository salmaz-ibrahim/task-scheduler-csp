
import json
import os

from google import genai
from dotenv import load_dotenv

load_dotenv()

#Gemini API
if not os.getenv("GEMINI_API_KEY"):
    raise ValueError("❌ GEMINI_API_KEY not found in .env file")

# Create Gemini client
client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

def parse_tasks_with_gemini(user_input):
    #User text to gemini
    prompt = f"""
    Extract tasks from the following text.

        Return ONLY valid JSON.

        Format:
        [
        {{
            "name": "Task name",
            "duration": number_of_hours,
            "priority": "low/medium/high"
        }}
        ]

        User input:
        {user_input}
        """
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt
    )

    #Clean possible markdown formatting
    cleaned_response = (
        response.text
        .replace("```json", "")
        .replace("```", "")
        .strip()
    )

    try:
        tasks = json.loads(cleaned_response)
        return tasks
    
    except json.JSONDecodeError:
        print(cleaned_response)
        return {"status": "error", 
                "message": "❌ Failed to parse tasks from AI response."}