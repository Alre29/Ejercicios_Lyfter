
little_list = [3,4,5,1,6,8]


def sum_list(items):
    sum = 0
    for index in items:
        sum += index
    
    return sum

print(sum_list(little_list))