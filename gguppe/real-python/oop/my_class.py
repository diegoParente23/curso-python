
class MyClass(Exception):
    def __init__(self, message):
        super().__init__(message)


raise MyClass(message="An error occured")

