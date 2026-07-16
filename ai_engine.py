import requests

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
        
        Your purpose is to be a trustworthy second brain that helps with programming, studying, productivity, notes, weather, and everyday tasks.
        
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
        

