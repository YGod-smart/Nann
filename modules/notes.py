import json

class Notes:
    
    def __init__(self):
        self.notes = []
        self.load()
        
    def add_note(self, note):
        self.notes.append(note)
        return "Note saved."
    
    def show_notes(self):
        
        if not self.notes:
            return "No notes."
        
        result = ""
        
        for i, note in enumerate(self.notes, start=1):
            result += f"{i}. {note}\n"
            
        return result
    
    def save(self):
        with open("data/notes.json", "w") as file:
            json.dump(self.notes, file)