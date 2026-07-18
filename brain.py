from ai_engine import Ai
from module_loader import ModuleLoader
from commands import handle_command


class Brain:
    def __init__(self, memory):
        self.memory = memory
        
        loader = ModuleLoader()
        self.modules = loader.load_modules()
        
        self.ai = Ai()
    
    def think(self, user_input):

    # 1. Try all modules first
        for module in self.modules:

            if module.can_handle(user_input):
                return module.handle(user_input)

    # 2. Try built-in commands
        response = handle_command(user_input, self.memory)

        if response != "I don't understand.":
            return response

    # 3. Let AI understand the request
        intent = self.ai.understand(user_input)

        if intent["intent"] == "remember":

            self.memory.remember(
                intent["category"],
                intent["key"],
                intent["value"]
            )

            return f"I'll remember that your {intent['key']} is {intent['value']}."

    # 4. Normal conversation
        return self.ai.handle(user_input)