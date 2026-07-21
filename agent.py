from context import ContextBuilder
from commands import handle_command

class Agent:

    def __init__(self, ai, memory, modules, conversation):

        self.ai = ai
        self.memory = memory
        self.tools = modules
        self.context = ContextBuilder(memory)
        self.conversation = conversation
        
    def reply(self, answer):

        self.conversation.add(
            "assistant",
            answer
        )

        return answer

    def process(self, user_input):
        
        self.conversation.add(
            "user",
            user_input
        )
    # 1. Try tools
        for tool in self.tools.all().values():

            if tool.can_handle(user_input):
                return tool.handle(user_input)

    # 2. Try built-in commands
        response = handle_command(user_input, self.memory)

        if response != "I don't understand.":
            return self.reply(response)

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

            answer = f"I'll remember that your {nice_key} is {intent['value']}."

            return self.reply(answer)

    # 5. Recall memory
        if intent["intent"] == "recall":

            memory = self.memory.search(intent["key"])

            if memory:

                nice_key = memory["key"].replace("_", " ")

                answer = f"Your {nice_key} is {memory['value']}."

                return self.reply(answer)
        
        # Weather
        if intent["intent"] == "weather":

            weather = self.tools.get("weather")

            weather_data = weather.get_weather(intent["city"])

            answer = self.ai.answer_weather(
                user_input,
                weather_data
            )

            return self.reply(answer)

# Internet
        if intent["intent"] == "internet":

            internet = self.tools.get("internet")

            search_result = internet.search(intent["query"])

            answer = self.ai.answer_search(
                user_input,
                search_result
            )

            return self.reply(answer)

# Normal conversation
        context = self.context.build()

        answer = self.ai.answer_normal(
            user_input,
            context
        )

        return self.reply(answer)

