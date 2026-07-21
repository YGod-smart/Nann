
class ContextBuilder:

    def __init__(self, memory):

        self.memory = memory

    def build(self):

        context = ""

        for item in self.memory.memories:

            context += f"{item['key']}: {item['value']}\n"

        return context