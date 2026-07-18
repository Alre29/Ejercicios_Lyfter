


#for number in list_of_numbers:
#    counter = 0
#    for i in range(number):
#    
#        if i != 0 and number % i == 0:
#            counter += 1
#        
#    if counter < 2:
#        list_of_primes.append(number)


#print(list_of_primes)

list_of_numbers =[1,2,6,4,12,21,23,31,25,34171,5,17]

def get_prime(list_items):
    list_of_primes = []
    for item in list_items:

        if item < 2: 
            continue    

        counter = 0

        for i in range(item):
            if i != 0 and item % i == 0:
                counter += 1 
        if counter < 2:
            list_of_primes.append(item)
    return list_of_primes


result = get_prime(list_of_numbers)

print(result)