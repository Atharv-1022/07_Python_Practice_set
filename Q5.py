'''Create a class Book with attributes title and author.

Implement __str__() so that printing the object displays "Title by Author".
Implement __len__() so that len(book) returns the length of the title.'''

class Book:
    def __init__(self,title,auhtor):
        self.title=title
        self.auhtor=auhtor

    def __str__(self):
        return f"{self.title} by {self.auhtor}"

    def __len__(self):
        return len(self.title)

B=Book("Nothing","Atharv")
print(B.__len__())
print(B.__str__())

#Create two Book objects and test these methods.
B2=Book("Java","Jone Doe")
print(B2.__str__())
print(B2.__len__())