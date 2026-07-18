my_list = ['4','hello','10','31','5.2','67']

def transform_to_int(items):

    for item in items:
        try:
            converted_number= int(item)
            print(f'"{item}" converted to {converted_number}')
            
        except ValueError as err:
            print(f"the element could not be converted: {item}")


transform_to_int(my_list)