the_string = 'Willow Y Arthur'

def print_reversed_string(the_string):
    new_string = ''

    for index in range(len(the_string)-1,-1,-1):
        new_string += the_string[index] #immutability
    
    return(new_string)
        

        
print(print_reversed_string(the_string))