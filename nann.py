from memory import Memory
from commands import handle_command


class Nann:
    def __init__(self):
        self.name = "Nann"
        self.memory = Memory()
        
    def run(self):
        print(f"{self.name} is online")
        
        while True:
            user_input = input("You: ")
            
            if user_input.lower() == "exit":
                print("Nann: Shutting down...")
                break
            
            response = handle_command(user_input, self.memory)
            
            print(f"Nann: {response}")