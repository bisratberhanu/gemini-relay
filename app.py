import os
import google.generativeai as genai
from flask import Flask, request, jsonify

# Initialize the Flask app
app = Flask(__name__)


# Configure the Gemini API key from an environment variable
# We will set this in the Render dashboard later
try:
    gemini_api_key = os.environ.get("GEMINI_API_KEY")
    if not gemini_api_key:
        # This error will be visible in the Render logs if the key is missing
        raise ValueError("GEMINI_API_KEY environment variable not set!")
    genai.configure(api_key=gemini_api_key)
except ValueError as e:
    # Print the error to the console when the app starts
    print(f"Error initializing Gemini: {e}")



# Define the model to use
MODEL_NAME = "gemma-3-27b-it"
model = genai.GenerativeModel(MODEL_NAME)
# gemini-2.5-flash
# This is the endpoint your client will call
@app.route('/generate', methods=['POST'])
def generate_text():
    # 1. Get the prompt from the incoming request
    # We expect the client to send a JSON body like: {"prompt": "Hello world"}
    if not request.json or 'prompt' not in request.json:
        # Return an error if the request is badly formatted
        return jsonify({"error": "Request must be JSON with a 'prompt' key"}), 400

    prompt = request.json['prompt']

    try:
        # 2. Call the Gemini API
        response = model.generate_content(prompt)

        # 3. Return Gemini's response to the client
        return jsonify({"response": response.text})

    except Exception as e:
        # If anything goes wrong with the Gemini API call, return a server error
        print(f"An error occurred: {e}")
        return jsonify({"error": "Failed to generate content from Gemini API"}), 500

# This allows the server to run
if __name__ == '__main__':
    # The port is set by the hosting provider (like Render)
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)
