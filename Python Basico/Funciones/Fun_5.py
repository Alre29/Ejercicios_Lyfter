string_one = 'I love Nation Sushi'

def count_upper_cases(string):
    counter_isupper = 0
    for index in range(len(string)):
        if string[index].isupper():
            counter_isupper += 1
    return counter_isupper

def count_lower_cases(string):
    counter_islower = 0
    for index in range(len(string)):
        if string[index].islower():
            counter_islower += 1
    return counter_islower



print(f'There are {count_upper_cases(string_one)} upper cases and {count_lower_cases(string_one)} lower cases')
