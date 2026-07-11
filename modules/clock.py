
from datetime import datetime

class Clock:
    def get_time(self):
        return datetime.now().strftime("%I:%M:%S %p")
    
    def get_date(self):
        return datetime.now().strftime("%B %d, %Y")