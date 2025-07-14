#functions 


# #this function is just for greeting the user....
# def welcome():
#     print('Hello Welcome to my Game!!!')
    
# #don't forget to call the function...
# welcome() 



#Example 2:  using and passing the arguments 


def welcome_with_name(name):
    print(f'Hello {name} Welcome to my Game!!!')

#don't forget to call the function...
welcome_with_name('John')  #john as an argumnet 
welcome_with_name('Jack')  #john as an argumnet 



#example 3: Some cal

def add (num1, num2):
    sum = num1 + num2
    print('Sum :', sum)
    
#calling the add function
add(1,1)
add(1,5)



def std_info(f_name, l_name):
    print(f_name)
    print(l_name)
    
#calling....
std_info(l_name='l', f_name='Jack')

    

    
    


