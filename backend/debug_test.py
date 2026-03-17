import os
import sys

print("Python version:", sys.version)
print("Current working directory:", os.getcwd())

# Test environment loading
def _simple_load_dotenv(dotenv_path="../.env"):
    print(f"Looking for .env file at: {os.path.abspath(dotenv_path)}")
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
        print("✅ .env file loaded successfully")
    except FileNotFoundError:
        print("❌ .env file not found")

_simple_load_dotenv()

print("NVIDIA_API_KEY:", os.getenv("NVIDIA_API_KEY"))

# Test openai import
try:
    from openai import OpenAI
    print("✅ OpenAI imported successfully")
    
    client = OpenAI(
        base_url="https://integrate.api.nvidia.com/v1",
        api_key=os.getenv("NVIDIA_API_KEY")
    )
    print("✅ OpenAI client created successfully")
    
except ImportError as e:
    print("❌ Failed to import OpenAI:", e)
