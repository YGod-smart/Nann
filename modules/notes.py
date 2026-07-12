import json

class Notes:
    
    def __init__(self):
        self.notes = []
        self.load()
        
    def add_note(self, note):
        self.notes.append(note)
        self.save()
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
            json.dump(self.notes, file, indent=4)
            
    def load(self):
        try:
            with open("data/notes.json", "r") as file:
                self.notes = json.load(file)
        
        except FileNotFoundError:
            self.notes = []
            
    def delete_note(self, index):
        
        if 1 <= index <= len(self.notes):
            deleted = self.notes.pop(index - 1)
            self.save()
            return f"Deleted note: {deleted}"
        
        return "Invalid note number."