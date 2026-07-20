my_list = [4,2,7,2,8,2,1,2,9]

number_to_find = 2

count = 0

for number in my_list: # Iterate through each number in the list
    if number == number_to_find: 
        count += 1 # Increment the count if the number matches the number we are looking for
        
print(f"The number {number_to_find} appears {count} times in the list.")
