from ai_engine import Ai
from module_loader import ModuleLoader
from agent import Agent
from conversation_memory import ConversationMemory

class Brain:

    def __init__(self, memory):

        self.memory = memory

        self.ai = Ai()

        loader = ModuleLoader()
        self.tools = loader.load_modules()
        
        self.conversation = ConversationMemory()

        #print(type(self.modules))  # temporary test

        self.agent = Agent(
            self.ai,
            self.memory,
            self.tools,
            self.conversation
        )

    def think(self, user_input):

        return self.agent.process(user_input)
    