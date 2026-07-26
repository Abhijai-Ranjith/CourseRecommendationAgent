from openai import OpenAI

client = OpenAI(
    api_key="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",
    base_url="https://api.groq.com/openai/v1"
)

response = client.chat.completions.create(
    model="llama-3.1-8b-instant",
    messages=[
        {"role": "user", "content": "Hello!"}
    ]
)

print(response.choices[0].message.content)
