#code to take the list a= [1,4,9,16,25,36,49,64,81,100] and makes a new list that has only even elements of this list in it.

a= [1,4,9,16,25,36,49,64,81,100]

#new list containing only even numbers

even_numbers_list = [x for x in a if x%2==0]

print (even_numbers_list)