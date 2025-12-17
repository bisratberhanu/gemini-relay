import google.generativeai as genai
import dotenv

#load api_key
API_KEY = dotenv.get_key(".env", "GEMENI_API_KEY")
genai.configure(api_key=API_KEY)
models = genai.list_models()
for model in models:
    print(model.name, model.supported_generation_methods)