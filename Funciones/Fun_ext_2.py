words_list = ['sky','root','oceans','floor','pie','sun','moon','stars','houses']
len_word = int(input('Enter the minimum character count:'))

def word_length_checker(words_list,len_word):
    filtered_list = []
    for word in words_list:
        if len(word) >= len_word :
            filtered_list.append(word)
    return filtered_list


result = (word_length_checker(words_list,len_word))
print(result)