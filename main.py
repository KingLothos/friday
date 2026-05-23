import os
from dotenv import load_dotenv
from google import genai

# Load environment variables from the .env file
load_dotenv()

# Retrieve the API key from the environment
api_key = os.environ.get("GEMINI_API_KEY")

# Safety guardrail check
if api_key is None:
    raise RuntimeError("GEMINI_API_KEY is not set in the environment variables.")

# Initialize the Gemini API client
client = genai.Client(api_key=api_key)

# Generate content using the gemini-2.5-flash model
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum."
)

# Print the text response payload
print(response.text)
