import os
import argparse
from dotenv import load_dotenv
from google import genai
from google.genai import types

# Load environment variables from the .env file
load_dotenv()

# Retrieve the API key from the environment
api_key = os.environ.get("GEMINI_API_KEY")

# Safety guardrail check
if api_key is None:
    raise RuntimeError("GEMINI_API_KEY is not set in the environment variables.")

# Set up the argument parser
parser = argparse.ArgumentParser(description="Chatbot")
parser.add_argument("user_prompt", type=str, help="User prompt")
args = parser.parse_args()

# Initialize the Gemini API client
client = genai.Client(api_key=api_key)

# ---- NEW CODE FOR L6: MULTIPLE MESSAGES ----
# Structure the prompt into a list of Content objects
messages: list[types.Content] = [
    types.Content(
        role="user",
        parts=[types.Part(text=args.user_prompt)]
    )
]

# Generate content using the structured list of messages
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=messages
)
# ---------------------------------------------

# Verify usage_metadata is present
if response.usage_metadata is None:
    raise RuntimeError("API request failed: No usage metadata returned.")

# Print the token counts
print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

# Print the text response payload
print(response.text)
