class StringReverser:
    def __init__(self, text):
        self.text = text

    def reverse(self):
        return self.text[::-1]


# Example usage:
s = StringReverser("Hello World")
print(s.reverse()) 
