
##Configure your list or tuple. For string/int/whatever in *the name of your list or tuple*
## print the string/int. 

list = [1,2,3,4,5]
for int in list:
    print(int)

## Adding an if break statement will stop the loop should a value be matched.    

list = [1,2,3,4,5,6,7,8,9]
for int in list:
    if int == 7:
        break   ##stops the loop
    else:
        print(int)
        
list = [1,2,3,4,5,6,7,8,9]
for int in list:
    if int == 7:
        continue ##skips the selection and continues the loop
    else:
        print(int)

##You can include an "else" statement at the end of the loop. Once the loop becomes
##false, it'll run your else command    

list = [1,2,3,4,5,6,7,8,9]
for int in list:
    if int == 7:
        continue ##skips the selection and continues the loop
    else:
        print(int)
else: 
    print("That is all")
