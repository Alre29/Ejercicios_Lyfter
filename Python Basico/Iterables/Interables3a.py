my_list = [4, 3, 6, 1, 7] 
first_element = my_list[0] #Guardamos el primer elemento de la lista en una variable
last_element = my_list[len(my_list)-1]#Guardamos el último elemento de la lista en una variable, para esto se resta 1 al largo de la lista, ya que los indices comienzan en 0

my_list[0] = last_element #Reemplazamos el primer elemento de la lista por el último
my_list[len(my_list)-1] = first_element #Reemplazamos el último elemento de la lista por el primer elemento 

print(my_list) #Imprimimos la lista con los elementos intercambiados