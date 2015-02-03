## Operators come in many varieties. Arithmetic, logical, assignment, comparison
##identity, etc.  

##Basic arithmetic operators. Begin by assigning 2 variables a value

a = 35
b = 25



print(a + b, 'This is the value of a plus b')
print(a - b, 'This is the value of a minus b')
print(a * b, 'This is the value of a times b')
print(a / b, 'This is the value of a divided by b')
print(a % b, 'This is the value of a divided b with remainder')
print(a ** b, 'This is the value of a to the power of b')


##Comparison Operators

c = 2
d = 4

e = 'Hello World'
f = 'Hello World'

print (c == d, 'This checks if the two variables are equal')
print (e == f, "This also works with strings")

print (c != d, 'This checks if the two variables are NOT equal')
print (c > d, 'This checks if the left operands is greater than the right')
print (c < d, 'This checks if the right operands is greater than the left')
print (c >= d, 'This checks if the left operands is greater than or equal to the right')
print (c <= d, 'This checks if the right operands is greater than or equal to the left')

## Logical operators 

g = 20
h = 10
i = 15

print(True if g and h > i else False) #This checks to see if both g and h are greater than i
print(True if g or h < i else False) #This checks to see if either g and h are less than to i

## Membership OperatorsTest
## In Python you can reference data lying in a sequence, using a membership operator

list = [1,2,3,4,5,6,7,8,9]
for int in list:
   print(int)  # For the int in the sequence, print the int. You can expand on this and call out data
   
list = [1,2,3,4,5,6,7,8]
for int in list:
    if int > 5:
        break
    else:
        print(int)
