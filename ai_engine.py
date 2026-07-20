import requests
import json

class Ai:
    def __init__(self):
        self.history = []
    
    def can_handle(self, user_input):
        return True
    
    def handle(self, user_input):
        return self.ask(user_input)
    
    def ask(self, question):
        url = "http://127.0.0.1:1234/v1/chat/completions"
        
        headers = {
            "Content-Type": "application/json"
        }
        messages = [
            {
                "role": "system",
                "content": """
        You are Nann, A personal AI assistant.
        
        You were created from scratch by your developer.
        
        Your purpose is to be a trustworthy second brain that helps with programming, studying, productivity, notes, weather, everyday tasks, and almost anything the user ask.
        
        Your personality:
        - Friendly and calm.
        - Clear and concise.
        - Honest when you don't know something.
        - Never make up facts.
        - Explain things simply.
        - Encourage learning instead of just giving answer.
        
        You know you are Nann.
        Your name is come from the burmese girl name.
        Do not invent facts about your creator or your history. If you don't know, say you don't know.
        """
            },
        ]
        messages.extend(self.history)
        
        messages.append(
            {
                "role": "user",
                "content": question
            }
        )
        
        data = {
            "model": "local-model",
            "messages": messages,
            "temperature": 0.7
        }
        
        
        try:
            response = requests.post(url, headers=headers, json=data)
            
            result = response.json()
            answer = result["choices"][0]["message"]["content"]
            
            self.history.append(
                {
                    "role": "user",
                    "content": question
                }
            )
            
            self.history.append(
                {
                    "role": "assistant",
                    "content": answer
                }
            )
            if len(self.history) > 20:
                self.history = self.history[-20:]
                
            return answer
        
        except Exception as e:
            return str(e)
        
    def understand(self, text):

        url = "http://127.0.0.1:1234/v1/chat/completions"

        headers = {
            "Content-Type": "application/json"
        }

        messages = [
            {
                "role": "system",
                "content": """
    You are Nann's intent analyzer.

    You NEVER answer the user.

    Your ONLY job is to analyze the user's message and return JSON.

    If the user wants you to remember personal information, return:

    {
        "intent":"remember",
        "category":"personal or preference",
        "key":"short_snake_case_key",
        "value":"the value"
    }

    Examples:

    User:
    My favorite language is Python.

    Output:
    {
        "intent":"remember",
        "category":"preference",
        "key":"favorite_language",
        "value":"Python"
    }

    User:
    I was born in Bagan.

    Output:
    {
        "intent":"remember",
        "category":"personal",
        "key":"birthplace",
        "value":"Bagan"
    }

    User:
    My birthday is May 7.

    Output:
    {
        "intent":"remember",
        "category":"personal",
        "key":"birthday",
        "value":"May 7"
    }

    If the message is NOT something to remember, return ONLY:

    {
        "intent":"chat"
    }

    Return ONLY JSON.

    Never explain.
    Never use markdown.
    Never add extra text.
    
    If the user is asking about previously remembered information:

    Example:

    User:
    What is my favorite language?

    Output:

    {
        "intent":"recall",
        "key":"favorite_language"
    }

    Example:

    User:
    Where was I born?

    Output:

    {
        "intent":"recall",
        "key":"birthplace"
    }
    
    If the user asks about weather:

    User:
    What is the weather in Tokyo?

    Output:

    {
        "intent": "weather",
        "city": "Tokyo"
    }

    User:
    Will it rain in Yangon today?

    Output:

    {
        "intent": "weather",
        "city": "Yangon"
    }
    
    If the user wants to search the internet:

    User:
    Search Python decorators

    Output:

    {
        "intent": "internet",
        "query": "Python decorators"
    }
    """
            },
            {
                "role": "user",
                "content": text
            }
        ]

        data = {
            "model": "local-model",
            "messages": messages,
            "temperature": 0
        }

        try:

            response = requests.post(
                url,
                headers=headers,
                json=data
            )

            result = response.json()

            return json.loads(
                result["choices"][0]["message"]["content"]
            )

        except Exception:

            return {
                "intent": "chat"
            }   
        

