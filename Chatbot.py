import openai

openai.api_key "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"

def chat_with_gpt(prompt):
    response openai.ChatCompletion.create(
      model="gpt-4.0", 
      messages=[{"role": "user", "content": prompt}]
    )

return response.choices[0].message.content.strip()

if __name__ = "__main__":
    while True:
        user_input input("You: ")
        if user_input.lower() in ["quit", "exit", "bye"]:
        break

        response chat_with_gpt(user_input)
        print("Chatbot: ", response)