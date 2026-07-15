import requests

class Ai:
    def __init__(self):
        pass
    
    def can_handle(self, user_input):
        return user_input.lower().startswith("ask ")
    
    def handle(self, user_input):
        question = user_input[4:]
        
        return self.ask(question)
    
    def ask(self, question):
        return f"You asked: {question}"