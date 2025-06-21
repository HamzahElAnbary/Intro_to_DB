class Calculator:
    calculation_type = "Arithmetic Operations"  # Class attribute

    @staticmethod
    def add(a, b):
        """Static method: adds two numbers without using class context."""
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """Class method: uses class context to access class attributes."""
        print(f"Calculation type: {cls.calculation_type}")
        return a * b
