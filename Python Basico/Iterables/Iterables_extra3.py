my_list = [-4,2,7,2,8,-1,11]
auxiliar = 0
minimum = my_list[0] # Initialize minimum with the first element of the list

for number in range(len(my_list)):
    auxiliar = my_list[number] # Get the current number from the list using its index
    if auxiliar <= minimum: # Compare the current number with the minimum found so far
        minimum = auxiliar  # Update minimum if the current number is smaller or equal to the current minimum
      
print(f"The minimum number in the list is: {minimum}"  )