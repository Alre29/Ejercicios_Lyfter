my_list = [4,2,7,2,8,11]
flag = True

for number in my_list:
    if number <= 0:
        flag = False
    
        
if flag:        
    print("All numbers are positive number in the list.")
else:
    print("There is at least one non-positive number in the list.")
    
