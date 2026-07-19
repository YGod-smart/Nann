
from commands import handle_command

class Agent:

    def __init__(self, ai, memory, modules):

        self.ai = ai
        self.memory = memory
        self.modules = modules

    def process(self, user_input):

    # 1. Try modules
        for module in self.modules.values():

            if module.can_handle(user_input):
                return module.handle(user_input)

    # 2. Try built-in commands
        response = handle_command(user_input, self.memory)

        if response != "I don't understand.":
            return response

    # 3. Understand the user's intent
        intent = self.ai.understand(user_input)

    # 4. Save memory
        if intent["intent"] == "remember":

            self.memory.remember(
                intent["category"],
                intent["key"],
                intent["value"]
            )

            nice_key = intent["key"].replace("_", " ")

            return f"I'll remember that your {nice_key} is {intent['value']}."

    # 5. Recall memory
        if intent["intent"] == "recall":

            memory = self.memory.search(intent["key"])

            if memory:

                nice_key = memory["key"].replace("_", " ")

                return f"Your {nice_key} is {memory['value']}."

            return "I don't remember that yet."

    # 6. Normal AI conversation
        return self.ai.handle(user_input)
