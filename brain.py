from module_loader import ModuleLoader
from commands import handle_command


class Brain:
    def __init__(self, memory):
        self.memory = memory
        
        loader = ModuleLoader()
        self.modules = loader.load_modules()
    
    def think(self, user_input):
        
        for module in self.modules:

          if module.can_handle(user_input):
             return module.handle(user_input)
        
        return handle_command(user_input, self.memory)