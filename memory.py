import json
import os


class Memory:

    def __init__(self):
        self.memories = []
        self.load()

    def remember(self, category, key, value):

        for memory in self.memories:

            if memory["key"] == key:
                memory["category"] = category
                memory["value"] = value
                self.save()
                return f"I updated your {key}."

        new_memory = {
            "category": category,
            "key": key,
            "value": value
        }

        self.memories.append(new_memory)
        self.save()

        return f"I'll remember your {key}."

    def recall(self, key):

        for memory in self.memories:

            if memory["key"] == key:
                return memory["value"]

        return "I don't know."

    def forget(self, key):

        for memory in self.memories:

            if memory["key"] == key:
                self.memories.remove(memory)
                self.save()
                return f"I forgot your {key}."

        return f"I don't know your {key}."

    def list_all(self):
        return self.memories

    def save(self):

        with open("data/memory.json", "w") as file:
            json.dump(self.memories, file, indent=4)

    def load(self):

        if not os.path.exists("data/memory.json"):
            self.memories = []
            return

        try:
            with open("data/memory.json", "r") as file:
                self.memories = json.load(file)

        except json.JSONDecodeError:
            self.memories = []
            
    def search(self, key):

        for memory in self.memories:

            if memory["key"] == key:
                return memory

        return None