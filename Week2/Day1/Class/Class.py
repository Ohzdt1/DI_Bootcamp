#project oriented programing 


# class Dog:
#     def __init__(self, name, color, breed, floppy_ears):
#         print("A new dog has been initialized !")
#         print("His name is", name)

#     # def __init__(self, color, breed, floppy_ears):
#         self.name = name
#         self.color = color 
#         self.breed = breed
#         self.floppy_ears = floppy_ears


#     def __str__(self):
#         return f"{self.name} is a, {self.breed}, {self.color}, {self.floppy_ears}"

# peanut = Dog('peanut', 'brown', 'mut', True) 

# print(peanut)

# Bagel = Dog('Bagel', 'white & Brown', "Begle", True)

# print(Bagel)




# class Person():
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age

# first_person = Person("John", 36)

# print(first_person.name)
# print(first_person.age)


# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

# ## create an instance of the class
# p = Point(3,4)

# ## access the attributes
# print("p.x is:", p.x)
# print("p.y is:", p.y)



# class Dog:
#     def __init__(self, name, color, breed, floppy_ears):
#         print("A new dog has been initialized !")
#         print("His name is", name)

#     # def __init__(self, color, breed, floppy_ears):
#         self.name = name
#         self.color = color 
#         self.breed = breed
#         self.floppy_ears = floppy_ears


#     def __str__(self):
#         return f"{self.name} is a, {self.breed}, {self.color}, {self.floppy_ears}"
    
#     def bark(self):
#         print(f"{self.name} barks WOOF!")

#     def walk(self, number_of_meters):
#         print(f"{self.name} walked {number_of_meters} meters")

#     def fetch(self, object):
#         print(f"{self.name} fetched a {object}")

#     def eat(self, food ):
#         print(f"{self.name} ate {food}")

#     def sit(self):
#         print(f"{self.name} sat down")

#     def rename(self, new_name):
#         self.name = new_name
#         print("The dogs new name is", new_name)


# peanut = Dog('peanut', 'brown', 'mut', True) 

# print(peanut)
# peanut.bark()
# peanut.fetch("ball")
# peanut.sit()

# peanut.eat('peanut butter')

# Bagel = Dog('Bagel', 'white & Brown', "Begle", True)

# print(Bagel)
# Bagel.bark()
# Bagel.bark()
# Bagel.fetch("ball")
# Bagel.sit()


# peanut.rename("peanut butter")


# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def show_details(self):
#         print("Hello my name is " + self.name)
    
#     def rename(self, new_name):
#         self.name = new_name

# first_person = Person("John", 36)
# first_person.show_details()
# first_person.rename("Peter")
# first_person.show_details()



# class Computer:

#     def description(self, name):
#         """
#         This is a totally useless function
#         """
#         print("I am a computer, my name is", name)
#         #Analyse the line below
#         print(self)

# mac_computer = Computer()
# mac_computer.brand = "Apple"
# print(mac_computer.brand)

# dell_computer = Computer()

# Computer.description(dell_computer, "Mark")
# # IS THE SAME AS:
# dell_computer.description("Mark")

class BankAccount:

    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance
        self.transactions = []

    def view_balance(self):
        self.transactions.append("View Balance")
        print(f"Balance for account {self.account_number}: {self.balance}")

    def deposit(self, amount):
        if amount <= 0:
            print("Invalid amount")
        elif amount < 100:
            print("Minimum deposit is 100")
        else:
            self.balance += amount
            self.transactions.append(f"Deposit: {amount}")
            print("Deposit Succcessful")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient Funds")
        else:
            self.balance -= amount
            self.transactions.append(f"Withdraw: {amount}")
            print("Withdraw Approved")
            return amount

    def view_transactions(self):
        print("Transactions:")
        print("-------------")
        for transaction in self.transactions:
            print(transaction)


