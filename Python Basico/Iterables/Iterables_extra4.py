my_list = [4,2,7,2,8,-1,11]
average = 0
new_list = []
sumatory = 0

for number in my_list:
    sumatory += number # Add each number in the list to the sumatory variable
    # Calculate the average by dividing the sumatory by the length of the list  
average = sumatory / len(my_list) 
for number in my_list:
    if number > average: # Check if the current number is greater than the average
        new_list.append(number) # If it is, add it to the new list

print(f"The average of the numbers in the list is: {average}")
print(f"The numbers greater than the average are: {new_list}")