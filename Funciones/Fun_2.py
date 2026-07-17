def test_local_scope():
    global internal_variable 
    internal_variable = 'Hello'

test_local_scope() # I must to call the function 

print(internal_variable)

def test_global_scope():
    print(f'Say {internal_variable}!') #Calling the  global variable 

test_global_scope()