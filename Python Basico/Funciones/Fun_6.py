my_string = 'function-computer-monitor-variable-python'

def get_string_parts(string): #Split the string by '-' and return a list
    new_list = string.split('-')

    return new_list



def get_sorted_items(items): #Receive the list and return a sorted list
    
    return sorted(items)


list_in_parts = get_string_parts(my_string)
sorted_list = get_sorted_items(list_in_parts)
result = '-'.join(sorted_list)

print(result)
