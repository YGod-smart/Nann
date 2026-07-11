from memory import Memory
from commands import handle_command
from brain import Brain

class Nann:
    def __init__(self):
        self.name = "Nann"
        self.memory = Memory()
        self.brain = Brain(self.memory)
        
    def run(self):
        print(f"{self.name} is online")
        
        while True:
            user_input = input("You: ")
            
            if user_input.lower() == "exit":
                print("Nann: Shutting down...")
                break
            
            response = self.brain.think(user_input)
            
            print(f"Nann: {response}")