from flask import Flask, request, jsonify
from openai import OpenAI
from openai import OpenAIError
import os
from dotenv import load_dotenv
import time

load_dotenv()

# Replace with your actual OpenAI API key
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
)
app = Flask(__name__)

# Define function descriptions for banking operations
function_descriptions = [
    {
        "name": "check_balance",
        "description": "Check user's bank balance",
        "parameters": {},
    }
]


@app.route('/banking', methods=['POST'])
def handle_banking_request():
    user_input = request.json['input']

    try:
        # Call OpenAI's API to generate a response
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",  # Update to the desired engine
            messages=[
                {
                    "role": "user",
                    "content": user_input,
                },
            ],
            functions=function_descriptions,
        )
        time.sleep(2)  # Introduce a delay of 2 seconds
        return jsonify({'response': response.choices[0].message.content.strip()})
    except OpenAIError as error:
        # Handle OpenAI errors here
        print(f"An error occurred: {error}")
        return jsonify({'error': 'Our assistant is currently experiencing technical difficulties. Please try again later.'})


if __name__ == '__main__':
    app.run(debug=True, port=5009)
