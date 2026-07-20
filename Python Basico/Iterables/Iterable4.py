my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even_list = []


for index in range(0, len(my_list)):
    if my_list[index] % 2 == 0: #Si el elemento en la posición index es par
        even_list.append(my_list[index]) #Se agrega a la segunda lista

print(even_list) #Imprimimos la segunda lista con los números pares