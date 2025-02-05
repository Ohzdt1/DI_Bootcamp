# #🌟 Exercise 1 : Convert lists into dictionaries

# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]

# new_dict = dict(zip(keys,values))
# print(new_dict)


# #🌟 Exercise 2 : Cinemax #2

# family = {}

# fam_members = int(input('How many are you today: '))

# def calculate_ticket_price(age):
#     if age < 3:
#         return 0
#     elif 3 <= age <= 12:
#         return 10
#     else:
#         return 15
     
# for _ in range(fam_members):
#     name = input("Enter the person's name: ")
#     age = int(input(f"Enter {name.capitalize()}'s age: "))
#     family[name] = age

# total_cost = 0
# for name, age in family.items():
#     price = calculate_ticket_price(age)
#     total_cost += price
#     print(f"{name.capitalize()} has to pay ${price}")

# print(f"Total cost for the family: ${total_cost}")

#🌟 Exercise 3: Zara
#1.Here is some information about a brand.
# 2. Create a dictionary called brand which value is the information from part one (turn the info into keys and values). The values type_of_clothes and international_competitors should be a list. The value of major_color should be a dictionary.

brand = {'name': 'Zara',
         'creation_date': 1975,
         'creator_name': 'Amancio Ortega Gaona',
         'type_of_clothes': ['men', 'women', 'children', 'home'],
         'international_competitors': ['Gap', 'H&M', 'Benetton'],
         'number_stores': 7000,
         'major_color' : {
            'France': 'blue',
            'Spain': 'red', 
            'US': ['pink', 'green']
        }
    }

print (brand)

#3. Change the number of stores to 2.
brand['number_stores'] = 2
print(brand)

#4. Use the key [type_of_clothes] to print a sentence that explains who Zaras clients are.
print('our target demographics are:', brand['type_of_clothes'])

#5. Add a key called country_creation with a value of Spain.
brand['country_creation'] = 'Spain'
print(brand)

#6. Check if the key international_competitors is in the dictionary. If it is, add the store Desigual.
if 'international_competitors' in brand:
    brand['international_competitors'].append('Desigual')

print(brand)

#7. Delete the information about the date of creation.
del brand ['creation_date']
print(brand)

#8. Print the last international competitor.
print(brand['international_competitors'][-1])

#9. Print the major clothes colors in the US.
print(brand['major_color']['US'])

#10. Print the amount of key value pairs (ie. length of the dictionary).
print("Number of key-value pairs in the dictionary:", len(brand))

#11. Print the keys of the dictionary.
print("Keys in the dictionary:", brand.keys())

#12. Create another dictionary called more_on_zara with the following details:
more_on_zara = {'creation_date': 1975, 
                'number_stores': 10000
                }

print(more_on_zara)

#13. Use a method to add the information from the dictionary more_on_zara to the dictionary brand.
brand.update(more_on_zara)

print(brand)

#14. Print the value of the key number_stores. What just happened ?
print(brand['number_stores'])


#Exercise 4 : Disney characters
users = ["Mickey","Minnie","Donald","Ariel","Pluto"]

disney_users_A = {}

for index, name in enumerate(users):
    disney_users_A[name] = index
print(disney_users_A)


disney_users_B = {}
for index, name in enumerate(users):
    disney_users_B[index] = name
print(disney_users_B)


sorted_users = sorted(users)
disney_users_C = {name: index for index, name in enumerate(sorted_users)}
print(disney_users_C)


disney_users_i = {}

index = 0

for name in users:
    if "i" in name:
        disney_users_i[name] = index
        index += 1
print(disney_users_i)


disney_users_mp = {}

for name in users:
    if name.startswith ('M') or name.startswith ('P'):
        disney_users_mp[name] = index
        index =+ 1

print(disney_users_mp)

