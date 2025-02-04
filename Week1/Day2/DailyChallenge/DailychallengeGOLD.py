#I used google and chatgpt tpo help me with this one 

import datetime

# Function to check if a year is a leap year
def is_leap_year(year):
    return (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0))

# Function to display the cake
def display_cake(candles):
    cake = f"""
       ___iiiii___
      |:H:a:p:p:y:|
    __|___________|__
   |^^^^^^^^^^^^^^^^^|
   |:B:i:r:t:h:d:a:y:|
   |{' ' * (17 - candles)}|
   ~~~~~~~~~~~~~~~~~~~
   """
    # Add the candles
    cake_with_candles = cake.replace(' ' * (17 - candles), '|' + 'I' * candles + '|')
    print(cake_with_candles)

# Ask the user for their birthdate
birthdate_input = input("Enter your birthdate (DD/MM/YYYY): ")

# Convert the input into a datetime object
birthdate = datetime.datetime.strptime(birthdate_input, "%d/%m/%Y")

# Get today's date
today = datetime.datetime.today()

# Calculate age
age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))

# Get the last digit of the age
candles = age % 10

# Check if the user was born in a leap year
if is_leap_year(birthdate.year):
    # Display two cakes if born in a leap year
    display_cake(candles)
    print("\n" + "=" * 20 + "\n")
    display_cake(candles)
else:
    # Display one cake otherwise
    display_cake(candles)


# I did not like that the cases on a leep year camne out cakes side by side cakes



    import datetime

# Function to check if a year is a leap year
def is_leap_year(year):
    return (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0))

# Function to display the cake
def display_cake(candles):
    cake = f"""
       ___iiiii___
      |:H:a:p:p:y:|
    __|___________|__
   |^^^^^^^^^^^^^^^^^|
   |:B:i:r:t:h:d:a:y:|
   |{' ' * (17 - candles)}|
   ~~~~~~~~~~~~~~~~~~~
   """
    # Add the candles
    cake_with_candles = cake.replace(' ' * (17 - candles), '|' + 'I' * candles + '|')
    return cake_with_candles

# Ask the user for their birthdate
birthdate_input = input("Enter your birthdate (DD/MM/YYYY): ")

# Convert the input into a datetime object
birthdate = datetime.datetime.strptime(birthdate_input, "%d/%m/%Y")

# Get today's date
today = datetime.datetime.today()

# Calculate age
age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))

# Get the last digit of the age
candles = age % 10

# Check if the user was born in a leap year
if is_leap_year(birthdate.year):
    # Display two cakes side by side if born in a leap year
    cake1 = display_cake(candles)
    cake2 = display_cake(candles)
    
    # Join the cakes side by side
    side_by_side = '\n'.join([f"{line1}   {line2}" for line1, line2 in zip(cake1.splitlines(), cake2.splitlines())])
    
    print(side_by_side)
else:
    # Display one cake if not born in a leap year
    print(display_cake(candles))



