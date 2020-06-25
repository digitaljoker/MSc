class Stack:
    def __init__(self):
        self.items = []
        
    def push(self, items):
        self.items.append(items)

    def pop(self):
        return self.items.pop()
            
    def peek(self):
        return self.items[-1]
   
    def is_empty(self):
        return self.items == []
            
items = []

num = int(input("Enter a number: "))

count = num
for x in range(count):

    if (num % 2) == 0:
      items.append(0)

    else:
      items.append(1)

    num = num // 2
    if num == 0:
        break
items.reverse()
print (items)    
