#a is an integer, assigned a value of 50. 
a = 50 
print(type(a),a)
#b is a float, assigned a value of 45.4
b = 45.4
print(type(b),b)
#c is a float, but we've told it it is an integer. It will completely negate the decimal
c = int (50.8)
print(type(c),c)
#d is an example of the round command. It will round a float to the nearest integer
d = round (50.8)
print(type(d),d)
#e is an integer, but we've told it it's a float
e = float(50)
print(type(e),e)
#f is a string. needs open and closing quoation marks to be valid
f = "This is a String"
print(type(f),f)
#g is a multi line string. Needs triple quotes. \ is an escape key, used for formatting
g = '''
Multi
Line 
String
'''
print(type(g),g)
#h using \n to break up single line strings into multi line strings 
h = "This is \na string" #if you use double \\ the \n will display
print(h)

#Inserting variables into strings. 
#To insert a different variable, change the letter after format
i = 'Zach'
k = 'Welcome, {}'.format(i)

print(k)

#Lists, class tuple() can't be modified. List [] can be modified.

x = (1,2,3,4,5)
print(type(x),x)

y = [1,2,3,4,5]
y.append(6)
print(type(y),y)

#Lists can declare an Index. Indexes start at 0. Number in the brackets is the counter for the list.
l = [1,2,3,4,5,6]
print(type(l),l[2])

#Lists, selecting ranges

m = [1,2,3,4,5,6]
print(type(m),m[1:3]) # Number 3 lands on 5. Last number is not counted

n = [1,2,3,4,5,6]
print(type(n),n[1:]) #Will count from #1 to the end. Can be used in reverse also

#Dictionary array. {} . Organized by hashing/memory order. There are ways to modify sorting.

#EX1
o = {'one':1, 'two':2, 'three':3}
print(type(o),o)
#EX2 Can be used to associate any combination of keys/variables
p = {'id':4, 'name':'Zach'}
print(p)

# Benefit of Lists over Arrays -> Lists get displayed in the same order as they're written

#EX3 - Another way of writing a Dictionary array. Keys no longer need quotes. 
dictionary = dict (
                   one = 1,
                   two = 'two'
                )
print(type(dictionary),dictionary)

#Boolean statements
a,b,c,d = 0,1,2,3
if a == b:
    print(True)
else:
    print(False)
    
