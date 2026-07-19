from ai_engine import Ai
from module_loader import ModuleLoader
from agent import Agent


class Brain:

    def __init__(self, memory):

        self.memory = memory

        self.ai = Ai()

        loader = ModuleLoader()
        self.modules = loader.load_modules()

        #print(type(self.modules))  # temporary test

        self.agent = Agent(
            self.ai,
            self.memory,
            self.modules
        )

    def think(self, user_input):

        return self.agent.process(user_input)
    