
def handle_command(command):
    if command == "help":
        return "Available commands...\n- help\n- about\n- exit"
        
    elif command == "about":
        return "Name: Nann\nVersion: 0.1\nDeveloper: YGod"
        
    else:
        return "I don't understand."