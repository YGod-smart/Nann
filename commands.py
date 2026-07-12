
def handle_command(user_input, memory):
    
    if user_input.startswith("remember my name is "):
        name = user_input.replace("remember my name is ", "")
        memory.remember("name", name)
        return "Okay I will remember your name!"
    
    elif user_input == "What is my name":
        return f"Your name is {memory.recall('name')}"
    
    elif user_input.startswith("remember my age is "):
        age = user_input.replace("remember my age is ", "")
        memory.remember("age", age)
        return "Okay I will remember your age!"
    
    elif user_input == "What is my age":
        return f"Your age is {memory.recall('age')}"
    
    elif user_input == "help":
        return "Available commands...\n- help\n- about\n- exit"
        
    elif user_input == "about":
        return "Name: Nann\nVersion: 0.3\nDeveloper: YGod"
    
    elif user_input.startswith("forget my "):
        key = user_input[10:]
        return memory.forget(key)
        
    else:
        return "I don't understand."