
from commands import handle_command
from modules.calculator import Calculator
from modules.clock import Clock
from modules.notes import Notes

class Brain:
    def __init__(self, memory):
        self.memory = memory
        self.calculator = Calculator()
        self.clock = Clock()
        self.notes = Notes()
        
        self.modules = [
            self.clock,
            self.notes,
            self.calculator
        ]
    
    def think(self, user_input):
        
        for module in self.modules:

          if module.can_handle(user_input):
             return module.handle(user_input)
        
        return handle_command(user_input, self.memory)