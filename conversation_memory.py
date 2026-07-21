import json
import os
from datetime import datetime


class ConversationMemory:

    def __init__(self):

        self.path = "data/conversations.json"
        self.history = []

        self.load()

    def add(self, role, message):

        self.history.append({
            "role": role,
            "message": message,
            "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })

        if len(self.history) > 100:
            self.history = self.history[-100:]

        self.save()

    def recent(self, amount=10):

        return self.history[-amount:]

    def save(self):

        with open(self.path, "w", encoding="utf-8") as file:
            json.dump(
                self.history,
                file,
                indent=4,
                ensure_ascii=False
            )

    def load(self):

        if not os.path.exists(self.path):
            return

        with open(self.path, "r", encoding="utf-8") as file:
            self.history = json.load(file)