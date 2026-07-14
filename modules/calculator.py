
class Calculator:
    def calculate(self, expression):
        try:
            result = eval(expression)
            return result
        
        except:
            return "Invalid math expression."
        
    def can_handle(self, user_input):
        math_symbols = ["+", "-", "*", "/", "(", ")"]

        return any(symbol in user_input for symbol in math_symbols)

    def handle(self, user_input):
        result = self.calculate(user_input)
        return f"The answer is {result}"