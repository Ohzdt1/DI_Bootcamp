# #Tuples: are immutable and Ordered - cannot be changed 

# numbers = (10, 20, 30, 40, 20, 50, 20)
# print(type(numbers))

# #numbers[1] = 25 - because its a tuple this will throw up an error 

# print(numbers[1])

# #methods
# print(numbers.count(20))
# print(numbers.index(30))

# #concatenate tuples
# numbers2 = (2,3,5,7)
# mixed_tuples = numbers + numbers2
# print (mixed_tuples)

# students = ['Juliana']
# print(students)

# my_tuple = (1,2)
# print(type(my_tuple))

# #unpacking a tuple
# a,b,c,d = (5,10,15,20)
# print(a)
# print(b)
# print(c)
# print(d)

# #example that you cam unpack variables of any type in python 
# name, age, email = 'Pinjas', 37, 'ohzdt1@gmail.com'
# print(name)


#Exercise

# a_tuple = (10, 20, 30, 40)

# a,b,c,d = a_tuple

# print(a)
# print(b)
# print(c)
# print(d)


#Sets = unordere data structure 

# my_set = {1,4,8,9}
# my_sets = set()

# my_set.add(12,)
# my_set.add(55,)
# print(my_set)

#print(my_set[1]) - this will throw up an error because it is unordered 

# id_numbers = [123,56,75634,235,123,5678,567,123]
# unique_ids = set(id_numbers)
# print(unique_ids)

# names = {'Juliana', 'Israel', 'Dina'}
# countries = {'USA', 'Brazil', 'Israel'}

# print(names.intersection(countries))

# names_and_countries = names.union(countries)

# print(names_and_countries)

# print(names.difference(countries))
# print(countries.difference(names))

# names.clear()
# print (names)


#EXERCIES
#Create a set of your favorite numbers. Write code that:
#Adds a new number to the set(using add()).
#Finds the common elements between two sets (use a set of your five favorite numbers and a set of prime numbers)
#Remove all elements from the set 

# new_set = {21,27,19,10,28,2}
# print(new_set)
# new_set.add(1)
# print(new_set)
# prime_numbers = {3,5,7,11}
# print(new_set.intersection(prime_numbers))
# prime_numbers.clear
# print(prime_numbers)


