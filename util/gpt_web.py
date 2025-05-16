import requests
import os
import re
def ask_gpt_web(messages, gpt_model,   url="http://127.0.0.1:5005/v1/chat/completions"):
    """
    Sends a chat request to the specified gpt_model endpoint.

    Args:
        gpt_model (str): The gpt_model name (e.g., "gpt-3.5-turbo").
        messages (list): A list of message dictionaries (e.g., [{"role": "user", "content": "Say this is a test!"}]).
        token (str): The authorization token for accessing the API.
        stream (bool): Whether to stream the response. Default is True.
        url (str): The URL of the API endpoint. Default is "http://127.0.0.1:5005/v1/chat/completions".

    Returns:
        Response object or generator: If `stream` is True, returns a generator for streamed responses.
                                      Otherwise, returns the full response as a JSON object.
    """
    print("***Asking GPT Web***")
    authorization = os.getenv('AUTHORIZATION', '').replace(' ', '')
        
    authorization_list = authorization.split(',') if authorization else []
    token = authorization_list[0]
    print("token:", token)
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}"
    }
    
    data = {
        "model": gpt_model,
        "messages": messages,
        "stream": False
    }
    try_times = 0
    while True:
    
        try:
            try_times += 1
            response = requests.post(url, headers=headers, json=data)
            response.raise_for_status()  # Raise an exception for HTTP errors
            completion = response.json()
            content = completion["choices"][0]["message"]["content"]
            if gpt_model not in completion["model"]:
                exit(0)
            pattern = r">Reasoning\n(.*?)\nReasoned .*? seconds\n(.*)"
            match = re.search(pattern, content, re.DOTALL)

            if match:
                reasoning_content = match.group(1).strip()
                after_reasoned_content = match.group(2).strip()

                # print("Reasoning Content:")
                # print(reasoning_content)
                # print("\nContent After Reasoned:")
                # print(after_reasoned_content)
            else:
                print("No match found on GPT WEB.")
                print(content)
                if "sorry" in content.lower() and try_times > 3:
                    final_output = {}
                    final_output["content"] = content
                    final_output["reasoning_content"] = "none"
                    
                    final_output["after_reasoned_content"] = content
                    print("***End Asking GPT Web***")
                    return final_output
                continue
            final_output = {}
            final_output["content"] = content
            final_output["reasoning_content"] = reasoning_content
            
            final_output["after_reasoned_content"] = after_reasoned_content
            print("***End Asking GPT Web***")
            return final_output
        
        except requests.exceptions.RequestException as e:
            continue
            print(f"An error occurred: {e}")
            return None

# Example usage
if __name__ == "__main__":
    # Example parameters
    gpt_model = "o4-mini"
    messages = [{"role": "user", "content": "Who I am?"}]
    # token = "your_token_here"  # Replace with your actual token

    # Call the function
    completion = ask_gpt_web(messages,gpt_model )
    print(completion)