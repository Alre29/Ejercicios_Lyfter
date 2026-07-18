phrase = input('Enter a phrase to use: ')

def vowels_counter(phrase):

    counter = 0
    vowels = 'aeiouAEIOU'

    for char in phrase:
        if char in vowels:
            counter += 1
    return counter



result = vowels_counter(phrase)

print(f'Number of vowels: {result}')