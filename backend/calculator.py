class Calculator:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def subtract(a, b):
        return a - b

    @staticmethod
    def multiply(a, b):
        return a * b

    @staticmethod
    def divide(a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

    @staticmethod
    def power(a, b):
        return a ** b

    @staticmethod
    def sqrt(a):
        if a < 0:
            raise ValueError("Cannot calculate square root of negative number")
        return a ** 0.5

    @staticmethod
    def evaluate(expression):
        try:
            # Basic expression evaluation (for more complex expressions, consider using eval with precautions)
            # This is a simple implementation - in production, you'd want a more robust expression parser
            return eval(expression, {"__builtins__": None}, {})
        except Exception as e:
            raise ValueError(f"Invalid expression: {str(e)}")