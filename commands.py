
def handle_command(user_input, memory):
    
    if user_input.startswith("remember my name is "):
        name = user_input.replace("remember my name is ", "")
        memory.remember("name", name)
        return "Okay I will remember your name!"
    
    elif user_input == "What is my name":
        return f"Your name is {memory.recall('name')}"
    
    elif user_input == "help":
        return "Available commands...\n- help\n- about\n- exit"
        
    elif user_input == "about":
        return "Name: Nann\nVersion: 0.1\nDeveloper: YGod"
        
    else:
        return "I don't understand."