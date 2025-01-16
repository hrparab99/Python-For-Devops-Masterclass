#This is single line comment

"""
This is 
Multi-Line 
Comment
"""

# Variables and Constants

2 #(Constant)

#Types of Data
a = 1       #<class 'int'>
b = 1.0     #<class 'float'>
c = "Harry" #<class 'str'>
d = False   #<class 'bool'>

print("\nValue of A =",a)
print("Value of B =",b)
print("Value of C =",c)
print("Value of D =",d)
print("\nclass of A =",type(a))
print("class of B =",type(b))
print("class of C =",type(c))
print("class of D =",type(d))

#Type Casting
print("\nType casting of A and B")
print("After type casting, class of A =",float(a),type(float(a)))
print("After type casting, class of B =",int(b),type(int(b)),"\n")

# Operators = which do operations as below

#Arithmetic Operators
x = 20
y = 10
add = x+y
sub = x-y
mul = x*y
div = x/y
print("Value of X =",x)
print("Value of Y =",y)
print("\nAddition of X and Y is",add)
print("Substraction of X and Y is",sub)
print("Multiplication of X and Y is",mul)
print("Division of X and Y is",div)

#Comparison Operators
print("X<Y =",x<y)
print("X>Y =",x>y)
print("X==Y =",x==y,"\n")