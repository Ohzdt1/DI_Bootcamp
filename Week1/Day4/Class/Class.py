# #Return 
# def calculate_total(price, quantity):
#     print('total', price * quantity)

# #print(type(calculate_total(5,12))) #nuneTupe

# calculate_total(5,12) #nothing is printed to the consol 
# print(calculate_total(5,2)) #result is printed on the console 

# def fav_color():
#     fav_color= ['blue','red','yellow']
#     for color in fav_color:
#         print (f'I love {color}')

#         return f'Those are my fav cololrs'
    
# print (fav_color())

#     #return mulktiple values 

# def get_country_info (country:str):
#         if country == 'Israel':
#             official_name = 'State of Israel'
#             capital = 'Jerusalem'
#             population = 10000000

#         elif country == 'Brazil':
#             official_name = 'Federative Republic of Brazil'
#             capital = 'Brazilia'
#             population = 21600000
#         else:
#             print('Invalid Country')
        
#         return official_name, capital, population
    
# print(get_country_info('Brazil'))

# official_name, capital, population = get_country_info('Brazil')

# print(f'''the official name of Brazil is{official_name}
#       the capital is {capital} and the population is {population}''')



#Global and Scope 

count_calculations = 100 #Global Scope 

def calculation(a, b, count_calculations):
    #  global count_calculations #option: global keyword
     addition = a + b
     subtraction = a - b
     count_calculations += 1
     return addition, subtraction

print(calculation(8, 5, count_calculations))
print(count_calculations)

clients = ['George', 'John', 'Lisa']

def welcome(client:list):
    for client in clients:
          print (f'Welcome {client}')
          clients[0] = 'Dave'
    # clients.append ('Maria')

def welcome_client():
     for client in clients:
          clients[0] = f'Hello {client}'

welcome(clients)
print(clients)

