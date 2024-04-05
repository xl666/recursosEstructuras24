#Variables
#A variable is a name attached to a value which can be changed and
#is used later in the code

#No need of declaration 

x = 10

#Data types

#Integer 
age = 21
players = 2
quantity = 5

#float (contains a decimal portion)
gpa = 3.2
distance = 2.5
price = 10.99

#String
name = 'Cris'
food = 'Pizza'
email = 'hola@gmail.com'

#Boolean (True or false)
online = True
for_sale = False
running = True

#example:
if running:
    print('Is running')
else:
    print('Is over')

#tips 
x, y, z = 1, 2, 3
x = y = z = 1 #Multiple variables to the same value

#f-string '{}' are acting as a place holder
print(f'your age is {age}')
print(f'There are {players} players in the game')
print(f'Would you like to buy {quantity} items')
print(f'Your gpa is = {gpa}')
