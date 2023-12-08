#!/usr/bin/env python3
import openai

def load_api_key(filepath):
    with open(filepath, 'r') as file:
        for line in file:
            if line.startswith('OPENAI_API_KEY='):
                return line.strip().split('=')[1]
    return None

def main():
    # Load OpenAI API key from config file
    api_key = load_api_key('config.txt')
    if not api_key:
        print("API key not found in config file.")
        return

    openai.api_key = api_key

    # Welcome message
    print("Welcome to the OpenAI Assistant. Type 'quit' to exit.")

    while True:
        # Get user input
        user_input = input("You: ")
        if user_input.lower() == 'quit':
            break

        # Create a request for the Assistant
        response = openai.Completion.create(
            model="gpt-4-1106-preview",
            prompt=user_input,
            max_tokens=150,
            stop=None
        )

        # Print the response from the Assistant
        print("Assistant:", response.choices[0].text.strip())

if __name__ == "__main__":
    main()
