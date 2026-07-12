import json

class Memory:
    def __init__(self):
        self.memories = {}
        self.load()
        
    def remember(self, key, value):
        self.memories[key] = value
        self.save()
            
    def recall(self, key):
        return self.memories.get(key, "I don't know.")
    
    def save(self):
            with open("data/memory.json", "w") as file:
                json.dump(self.memories, file, indent=4)
    
    def load(self):
        try:
            with open("data/memory.json", "r") as file:
                self.memories = json.load(file)
        
        except FileNotFoundError:
            self.memories = {}
            
    def forget(self, key):
        if key in self.memories:
            
            del self.memories[key]
            self.save()
            return f"I forgot your {key}."
        
        return f"I dont know your {key}."