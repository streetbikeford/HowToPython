##Try statements allow you to give user error messages

##tuples are basically read-only lists

##You specify a tuple. You TRY to append a value to the tuple. If what your trying does not work
##Python will run your except statement, which in this cause prints "Configuration Error".
##If what you try is successful, Python will skip except, and move onto your else statement.

tuple=(1,4,54,55)

try:
	tuple.append(45) ##If you just type tuple.append, this code will error out. 
except:
	print('Configuration Error')
else:
	for each in tuple:
		print(each)

## You can also move the else statement to follow the try and the code will run the same

tuple=(1,4,54,55)

try:
	tuple.append(45)      ## Your script will try to append the tuple, fail, and skip to except
	for each in tuple:
		print(each)
except:
	print('Configuration Error')


## Adding attributes to your error message. Will give you more detail concerning the error

tuple=(1,4,54,55)

try:
	tuple.append(45)      ## Your script will try to append the tuple, fail, and skip to except
	for each in tuple:
		print(each)
except AttributeError as e:  ## The error here is append is not an attribute of tuple. 
	print('Configuration Error', e)  

