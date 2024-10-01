class Calc:

    def __init__(self):
        pass

    def divide(self, a, b):

        self.a = a
        self.b = b
        
        try:
            self.result = self.a / self.b

        except TypeError:
            raise TypeError

        except ZeroDivisionError:
            raise ZeroDivisionError

        return self.result

    def multiply(self, a, b):

        self.a = a
        self.b = b

        try:
            self.result = self.a * self.b
        except TypeError:
            raise TypeError

        return self.result

    def sum(self, a, b):
        
        self.a = a
        self.b = b

        try:
            self.result = self.a + self.b

        except TypeError:
            raise TypeError

        return self.result

    def subtract(self, a, b):

        self.a = a
        self.b = b

        try:
            self.result = self.a - self.b

        except TypeError:
            raise TypeError

        return self.result
