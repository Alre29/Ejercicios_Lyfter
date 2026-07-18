my_list = [4, 3, 6, 1, 7] 
first_element = my_list[0] #Guardamos el primer elemento de la lista en una variable
last_element = my_list[len(my_list)-1]#Guardamos el último elemento de la lista en una variable, para esto se resta 1 al largo de la lista, ya que los indices comienzan en 0

for index in range(0, len(my_list)):
    if index == 0:
        print(last_element)#si el indice es igual a 0, se imprime el último elemento

    elif index == len(my_list)-1:
        print(first_element)#si el indice es igual al largo de la lista menos 1, se imprime el primer elemento
    else:
        print(my_list[index])#si el indice no es ni 0 ni el último, se imprime el elemento en esa posición


