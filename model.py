import requests
from langchain.schema.runnable import Runnable
import json

class MistralLLM(Runnable):
    """Custom LLM class to interact with Mistral with streaming support"""

    def __init__(self, model_name="mistral-large-latest", api_key="add_your_key"):
        self.api_key = api_key
        self.model_name = model_name
        self.api_url = "https://api.mistral.ai/v1/chat/completions"

    def invoke(self, prompt: str,*args, **kwargs):
        """Sends a request to Mistral API with streaming enabled"""
        if hasattr(prompt, "to_string"):  
            prompt = prompt.to_string()
        elif hasattr(prompt, "format"):  
            prompt = prompt.format()
        else:
            prompt = str(prompt)

        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        payload = {
            "model": self.model_name,
            "messages": [{"role": "user", "content": prompt}],
            "stream": True  # Enable streaming
        }
        response = requests.post(self.api_url, json=payload, headers=headers, stream=True)
        return self._process_stream(response)

    def _process_stream(self, response: requests.Response):
        """Handles streaming response from Mistral API"""
        collected_text = ""
        try:
            for line in response.iter_lines():
                if line:
                    try:
                        chunk = line.decode("utf-8").strip()
                      

                        # Ensure that the chunk starts with "data:", since your response has a "data:" prefix
                        if chunk.startswith("data:"):
                            chunk = chunk[5:].strip()  # Remove "data:" from the start

                        # Parse the JSON data
                        chunk_json = json.loads(chunk)
            
                        

                        # Check if there is content in the "choices" array
                        if "choices" in chunk_json and chunk_json["choices"]:
                            new_text = chunk_json["choices"][0]["delta"].get("content", "")
                           
                            collected_text += new_text

                        else:
                            print("No choices found or content missing.")
                    except json.JSONDecodeError:
                        print("Failed to decode JSON")
                        continue  # Ignore incomplete lines
        except Exception as e:
            print(f"Error: {str(e)}")
            return f"Error: {str(e)}"

        return collected_text