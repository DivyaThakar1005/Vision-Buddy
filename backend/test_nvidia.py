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
        # no .env file present; that's fine
        pass

_simple_load_dotenv()

# # Load variables from .env file
# load_dotenv()

client = OpenAI(
    base_url="https://integrate.api.nvidia.com/v1",
    api_key=os.getenv("NVIDIA_API_KEY")
)
response = client.chat.completions.create(
    model="nvidia/nemotron-mini-4b-instruct",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Say hello in one sentence."}
    ],
    temperature=0.2,
    max_tokens=100
)

print(response.choices[0].message.content)

# response = client.completions.create(
#     model="nvidia/llama-3.1-nemotron-70b-instruct",
#     prompt="Say hello in one sentence.",
#     max_tokens=100
# )

# print(response.choices[0].text)
# Test 1: Text model
# response = client.chat.completions.create(
#     model="nvidia/llama-3.1-nemotron-70b-instruct",
#     messages=[{"role": "user", "content": "Say hello in one sentence."}],
#     max_tokens=100
# )
# response = client.chat.completions.create(
#     model="nvidia/nvidia/llama-3.1-nemotron-70b-instruct",
#     messages=[{"role": "user", "content": "Say hello in one sentence."}],
#     max_tokens=100
# )
# print("✅ Nemotron works:", response.choices[0].message.content)
# try:
#     response = client.chat.completions.create(
#         model="nvidia/llama-3.1-nemotron-70b-chat",
#         messages=[{"role": "user", "content": "hello"}],
#         max_tokens=50
#     )
#     print(response.choices[0].message.content)

# except Exception as e:
#     print(e)

# print(os.getenv("NVIDIA_API_KEY"))

# models = client.models.list()

# for m in models.data:
#     print(m.id)


# models = client.models.list()

# for m in models.data:
#     print(m.id)


    