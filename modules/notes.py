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
    
    def can_handle(self, user_input):
        user_input = user_input.lower()

        return (
            user_input.startswith("take note ")
            or user_input == "show notes"
            or user_input.startswith("delete note ")
        )


    def handle(self, user_input):
        user_input = user_input.lower()

        if user_input.startswith("take note "):
            note = user_input[10:]
            return self.add_note(note)

        if user_input == "show notes":
            return self.show_notes()

        if user_input.startswith("delete note "):

            try:
                number = int(user_input[12:])
                return self.delete_note(number)

            except ValueError:
                return "Please enter a valid note number."