from openai import OpenAI
import os

def _simple_load_dotenv(dotenv_path="../.env"):
    try:
        with open(dotenv_path, "r") as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith("#"):
                    continue
                if "=" in line:
                    key, val = line.split("=", 1)
                    key = key.strip()
                    val = val.strip().strip('"').strip("'")
                    if key and key not in os.environ:
                        os.environ[key] = val
    except FileNotFoundError:
        pass

_simple_load_dotenv()

print("API Key loaded:", "Yes" if os.getenv("NVIDIA_API_KEY") else "No")

client = OpenAI(
    base_url="https://integrate.api.nvidia.com/v1",
    api_key=os.getenv("NVIDIA_API_KEY")
)

print("Client created successfully")

try:
    print("Making API request...")
    response = client.chat.completions.create(
        model="nvidia/llama-3.1-nemotron-70b-instruct",
        messages=[{"role": "user", "content": "Say hello in one word."}],
        max_tokens=10
    )
    print("✅ Success:", response.choices[0].message.content)

except Exception as e:
    print("❌ Error:", str(e))
    print("Error type:", type(e).__name__)
