#Name: Eamon Kelly; Student ID: S19003656; Due Date: 11th May 2020
#Code Assignment 1 Draw user specified number of regular Heptagons (50p's)
#Note Heptagon angles determined for this task interior: 128.57, exterior: 51.43

#import required libraries


#Class Definitions
class Stack:

    def __init__(self):
        self.items = []
        
    def is_empty(self):
        return self.items == []
    
    def peek(self):
        return self.items[-1]
    
    def pop(self):
        return self.items.pop()
    
    def push(self, item):
        self.items.append(item)
        
    def size(self):
        return len(self.items)
    

binarystr = []
workstack = Stack()
#Numeric value input required from user
positiveint = input("Input a positive integer number to convert to binary: ")
while not positiveint.isnumeric():
    positiveint = input("Please fool, input a positive integer number: ")
    
positiveint =abs(int(positiveint))
    
print("Thank you, your number {0} will be converted to binary".format(positiveint))

while positiveint != 0:
    if (positiveint % 2) == 0:
        workstack.push(0)
    else:
        workstack.push(1)
    positiveint = int(positiveint /2)
    
for digit in range(workstack.size()):
    binarystr.append(workstack.pop())

print(binarystr)
        