import ollama
response = ollama.chat(
    model="llama3.2:3b",
    messages=[
        {
            "role":"user",
            "content": "Give the defination of ai in two lines and three main types of ai also give three examples and provide each example with bullet points"
        }
    ]
)
print(response["message"]["content"])