
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
        
    def think(self, user_input):
        
        math_symbols = ["+", "-", "*", "/", "(", ")"]
        
        if any(symbol in user_input for symbol in math_symbols):
            result = self.calculator.calculate(user_input)
            return f"The answer is {result}"
        
        if user_input.lower() == "what time is it":
            return self.clock.get_time()
        
        if user_input.lower() == "what is today's date":
            return self.clock.get_date()
        
        if user_input.lower().startswith("take note "):
            note = user_input[10:]
            return self.notes.add_note(note)
        
        if user_input.lower() == "show notes":
            return self.notes.show_notes()
        
        if user_input.lower().startswith("delete note "):
            
            try:
                number = int(user_input[12:])
                return self.notes.delete_note(number)
            
            except ValueError:
                return "Please enter a valid note number."
        
        return handle_command(user_input, self.memory)