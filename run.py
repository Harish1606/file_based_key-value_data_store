#Importing Functions class from functions.py  
from functions import Functions

print("Enter 1 to create value in json file")
print("Enter 2 to read value in json file")
print("Enter 3 to delete value in json value")
print("Enter any other value to exit")
n=int(input())

obj=Functions()

if n==1:
    obj.create()
elif n==2:
    obj.read()
elif n==3:
    obj.delete()
else:
    exit()

while True:
    s=input('Do you want to continue enter yes/no: ')
    if s=='yes':        
        print("Enter 1 to create value in json file")   
        print("Enter 2 to read value in json file")
        print("Enter 3 to delete value in json value")
        print("Enter any other value to exit")
        n=int(input())
        if n==1:
            obj.create()
        elif n==2:
            obj.read()
        elif n==3:
            obj.delete()
        else:
            break 
    else:
        break