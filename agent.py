from context import ContextBuilder
from commands import handle_command

class Agent:

    def __init__(self, ai, memory, modules):

        self.ai = ai
        self.memory = memory
        self.modules = modules
        self.context = ContextBuilder(memory)

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
        
        if intent["intent"] == "weather":

            weather = self.modules["weather"]

            weather_data = weather.get_weather(intent["city"])

            prompt = f"""
            You are Nann.

            You already have the weather information below.

            Do NOT say you don't have access to live weather.
            Do NOT tell the user to check another website.
            Do NOT mention limitations.

            Your job is ONLY to answer using the provided weather information.

            Weather Information:

            {weather_data}

            User Question:

            {user_input}

            Answer naturally in one short paragraph.
            """

            return self.ai.ask(prompt)
        
        if intent["intent"] == "internet":

            internet = self.modules["internet"]

            search_result = internet.search(intent["query"])

            prompt = f"""
            The user asked:

            {user_input}

            Search result:

            {search_result}

            Answer naturally as Nann.
            Use only the information above.
            If the search result says nothing was found,
            tell the user honestly.
            """

            return self.ai.ask(prompt)

    # 6. Normal AI conversation
        return self.ai.handle(user_input)
