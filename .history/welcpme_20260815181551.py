x = 5
y=10
print(x)
print(y)

x="sam"
print(x)

#Casting
x=(5)
y=int(10)
z=float(20)

print (x,y,z)

print(type(x))

#Long Variable names
#Camelcase
aVariableId = 5

#Pascal case
BankCustomerId = 10001

#Snake case
Bank_Cust_ID = 2002

print (aVariableId,BankCustomerId,Bank_Cust_ID)



#Unpacking concept
Fruit = ("Apple","Mango","banana")
x,y,z= Fruit
print(x)
print(y)
print(z)

#How to output variables
x = "Biden is president"
print(x)

x="Biden"
y="is"
z="president"

print(x,y,z)
print (x,y,z)

#Global variables - used in/out of any function
x = "LOL"

def myfun():
    x="ROFL"
    print("Python is", x)

myfun()
    
print("Python is", x)