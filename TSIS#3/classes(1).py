class StringManipulation:
    def __init__(self):
        self.string = ""

    def getString(self):
        self.string = input("Enter a string: ")

    def printString(self):
        print(self.string.upper())

strObj = StringManipulation()
strObj.getString()
strObj.printString()
