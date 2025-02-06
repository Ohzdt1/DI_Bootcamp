# Args : not defined quantity of arguments 
#the important past of *args is the *the name can change 
def calculation(*nums):
    return sum(nums)
        
print(calculation(1,5, 3, 7))

#**kwargs 
#k- key w-words - args - arguments 

def get_user_info (**kwargs):
    print (kwargs)

get_user_info(name = 'John', last_name = 'Doe', age = 45, occupation = 'Engineer')

