special_word = input('Write your special word ')
char = input('Enter the character you want to count: ')

def letter_finder(word, letter):
    
    result = word.count(letter)
    return  result


total = letter_finder(special_word, char)

print(f'In your word "{special_word}", the character "{char}" appears {total} times.')