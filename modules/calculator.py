
class Calculator:
    def calculate(self, expression):
        try:
            result = eval(expression)
            return result
        
        except:
            return "Invalid math expression."