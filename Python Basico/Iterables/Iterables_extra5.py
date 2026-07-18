my_list = []

print  ("Please enter 5 words to add to the list.")
for index in range(5):  
    word = input(f'Enter a word: {index + 1} ')
    if len(word) > 4:
        my_list.append(word) # Add the word to the list if its length is greater than 5  my_list.append(word)  

print(f"The words in the list that have more than 5 characters are: {my_list}")