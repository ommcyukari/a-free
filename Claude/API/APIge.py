import anthropic
import os

api_key = os.getenv("ANTHROPIC_API_KEY")

client = anthropic.Anthropic(api_key=api_key)

message = client.messages.create(
    model="Claude-3.5-Sonnet-20241022",  
    max_tokens=8000,
    messages=[
        {
            "role": "user",
            "content": "Claudeについて教えてください"
        }
    ]
)

print(message.content) 

