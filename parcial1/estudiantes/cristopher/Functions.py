#Function = Block of reusable code 
#           Place () after the function name to invoke it

#Return = Statement used to end a function 
#         and send a result back to the caller 

#Exercise 1
def happy(name, age):
    print(f'Happy Happy Happy {name}')
    print(f'Your age is {age}')

#Exercise 2
def Information(name,bill,date):
   print(f'Hello {name} your bill is ${bill} and is due: {date}')

def name2(name, last_name):
    return name + ' ' + last_name

def function():
    global variable #Manera de indicar que las quieres usar como globales
    variable = 0

if __name__ == '__main__':
    name = (input())
    bill = (input())
    date = (input())
    Information(name,bill,date)
    nam2 = 'spongebob'
    last = 'squarepants'
    print(name2(nam2,last))
    happy('cris',20)
    function()
    print(variable)
#   Any data in the () are know as arguments