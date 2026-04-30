#New Google cloud sdk
from google import genai

client = genai.Client()

def get_time_slots_from_user():
    prompt = """
    Ask the user to provide 3 time blocks for their day.
    Example:
    - 9:00–11:00
    - 1:00–3:00
    - 6:00–8:00

    Return ONLY a comma-separated list.
    """
    response = client.models.generate_content(
        model = "gemini-2.0-flash",
        contents= prompt
    )
    return response.text.strip()