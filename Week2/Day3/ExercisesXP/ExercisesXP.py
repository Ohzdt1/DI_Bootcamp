class Currency:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount

    def __str__(self):
        return f"{self.amount} {self.currency}" + ("s" if self.amount > 1 else "")

    def __repr__(self):
        return self.__str__()

    def __int__(self):
        return self.amount

    def __add__(self, other):
        if isinstance(other, Currency):
            if self.currency != other.currency:
                raise TypeError(f"Cannot add between Currency type <{self.currency}> and <{other.currency}>")
            return Currency(self.currency, self.amount + other.amount)
        elif isinstance(other, (int, float)):
            return Currency(self.currency, self.amount + other)
        else:
            raise TypeError("Unsupported type for addition")

    def __iadd__(self, other):
        if isinstance(other, Currency):
            if self.currency != other.currency:
                raise TypeError(f"Cannot add between Currency type <{self.currency}> and <{other.currency}>")
            self.amount += other.amount
        elif isinstance(other, (int, float)):
            self.amount += other
        else:
            raise TypeError("Unsupported type for addition")
        return self
    

c1 = Currency('dollar', 5)
c2 = Currency('dollar', 10)
c3 = Currency('shekel', 1)
c4 = Currency('shekel', 10)

print(str(c1))
print(int(c1))
print(repr(c1))
print(int(c1) + 5)
print(c1 + c2)
print(c1)
c1 += c2
print(c1)
# try:
#     print(c1 + c3) 
# except TypeError as e:
#     print(e)



#🌟 Exercise 3: String module
#see files func.py and exercise_one.py in folder ExerciseXP




#🌟 Exercise 4 : Current Date

from datetime import datetime

def display_current_date():
    current_date = datetime.today().strftime("%Y-%m-%d")
    print("Today's date is:", current_date)


display_current_date()



#Exercise 5 : Amount of time left until January 1st
from datetime import datetime

def time_until_new_year():
    now = datetime.now()
    next_new_year = datetime(now.year + 1, 1, 1)
    time_left = next_new_year - now  

    days = time_left.days
    hours, remainder = divmod(time_left.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)

    print(f"The 1st of January is in {days} days and {hours}:{minutes}:{seconds} hours.")


time_until_new_year()


#Exercise 6 : Birthday and minutes


from datetime import datetime

def minutes_lived(birthdate_str):
    birthdate = datetime.strptime(birthdate_str, "%Y-%m-%d")  
    now = datetime.now()

    time_lived = now - birthdate
    minutes_lived = time_lived.total_seconds() / 60

    print(f"You have lived for approximately {int(minutes_lived):,} minutes.")

minutes_lived("1988-01-21")


#Exercise 7 : Faker Module
#first run pip install faker

from faker import Faker

fake = Faker()

users = []

def add_fake_user():
    user = {
        "name": fake.name(),
        "address": fake.address(),
        "language_code": fake.language_code(),
    }
    users.append(user)

for _ in range(5):
    add_fake_user()

for user in users:
    print(user)