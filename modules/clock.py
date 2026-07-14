
from datetime import datetime

class Clock:
    def can_handle(self, user_input):
        user_input = user_input.lower()
        return (
            user_input == "what time is it"
            or user_input == "what is today's date"
        )
    
    def handle(self, user_input):
        user_input = user_input.lower()
        
        if user_input == "what time is it":
            return self.get_time()
        
        if user_input == "what is today's date":
            return self.get_date()
        
    def get_time(self):
        return datetime.now().strftime("%I:%M:%S %p")

    def get_date(self):
        return datetime.now().strftime("%B %d, %Y")