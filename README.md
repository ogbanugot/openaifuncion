Description:

This Flask application demonstrates a basic banking assistant built with Flask and OpenAI's gpt-3.5-turbo large language model. It utilizes conversation history to simulate a chatbot interaction for users performing basic banking inquiries.

Features:

Conversation-based Interaction: Users can interact with the assistant through text input, mimicking a natural conversation flow.
OpenAI Integration: The gpt-3.5-turbo model generates responses based on user input and provided conversation history.
Function Descriptions (placeholder): While not currently implemented, the code includes function_descriptions to potentially integrate functionalities like balance checks.
Requirements:

Python 3.6 or later
Flask framework (https://flask.palletsprojects.com/)
OpenAI API key (https://platform.openai.com/login)
python-dotenv library (https://pypi.org/project/python-dotenv/)
Setup:

Clone this repository.
Install required libraries:
Bash
pip install flask openai python-dotenv
Use code with caution.
Create a file named .env in the project root directory.
Add your OpenAI API key to the .env file with the following format:
OPENAI_API_KEY=your_api_key
Replace your_api_key with your actual OpenAI API key.
Running the Application:

Open a terminal in the project directory.
Run the following command:
Bash
flask run
Use code with caution.
This will start the Flask development server, usually accessible at http://127.0.0.1:5000/.
Usage:

Send a POST request to the /banking endpoint with JSON data containing a key input that represents the user's query.
The application will process the input through the OpenAI API and generate a response that simulates a conversation.
Example Usage (using cURL):

Bash
curl -X POST http://localhost:5000/banking -H 'Content-Type: application/json' -d '{"input": "Can you tell me my balance?"}'
Use code with caution.
