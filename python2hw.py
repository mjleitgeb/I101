name = "Max Leitgeb" #sets my name to the variable "name"

namelen = len(name) #sets namelen equal to the number of characters in name

if namelen > 15:
    print("your name has more than 15 characters") #checks if name is longer than 15 characters
elif namelen < 10:
    print("Your name is less than 10 characters") #checks if name is shorter than 10 characters
else:
    print("Your name is in between 10 and 15 characters") #checks if name is in between 10 and 15 characters

x = 0

while x < len(name): #print each character in "name"
    print(name[x])
    x += 1
    
