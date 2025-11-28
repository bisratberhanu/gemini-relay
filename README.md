# Gemini Relay

This is a simple Flask application that acts as a relay to the Google Gemini API. It exposes a `/generate` endpoint that takes a prompt and returns a response from the Gemini `gemini-2.5-flash` model.

## How to Initialize the App

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/bisratberhanu/gemini-relay.git
    cd gemini-relay
    ```

2.  **Create a virtual environment and install dependencies:**

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```

3.  **Set the environment variable:**
    You need to set your Gemini API key as an environment variable.

    ```bash
    export GEMINI_API_KEY='your_gemini_api_key'
    ```

4.  **Run the application:**
    ```bash
    gunicorn app:app
    ```
    The application will start, and you can send POST requests to the `/generate` endpoint.

## Environment Variables

- `GEMINI_API_KEY`: **Required**. Your API key for the Google Gemini service.
- `PORT`: Optional. The port for the web server to listen on. Defaults to `8080` if not set, but `gunicorn` will use its own default (e.g., 8000) if the `PORT` variable isn't present.
