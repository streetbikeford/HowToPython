//WHILE LOOPS


//You begin with a = 50. While a , 100 you will print the value of a. 
//After every print, you will add 1 to add and recheck to see if it's <100
//If a is no longer <100, print the string "You have reached 100"

a = 50 

while a < 100:     
	print (a)
    a+=1
else:    
    print("You have reached 100")



//FOR LOOPS



// for data will read each character in your string individually. so for data //'hello' will print as 
//h
//e
//l
//l
//o
//The same is true of lists. If you enter the command for data in (a,v,s,g,w) and //print, you will list of each letter on it's own line.


for data in 'hello':
    print(data)


//This script will pull every third letter, starting with 1. Every 3rd letter is 
//an i 
    
for key,data in enumerate('Mississippi'):
    if key % 3 == 1:
       print('The letter {} is in a location divisible by 3'.format(data))