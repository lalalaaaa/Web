#!/usr/bin/env python3
from openai import OpenAI

client = OpenAI(api_key='YOUR_API_KEY')

def main():
    # Set your OpenAI API key

    # Welcome message
    print("Welcome to the OpenAI Assistant. Type 'quit' to exit.")

    while True:
        # Get user input
        user_input = input("You: ")
        if user_input.lower() == 'quit':
            break

        # Create a request for the Assistant
        response = client.completions.create(model="gpt-4-1106-preview",
        prompt=user_input,
        max_tokens=150,
        stop=None)

        # Print the response from the Assistant
        print("Assistant:", response.choices[0].text.strip())

if __name__ == "__main__":
    main()

