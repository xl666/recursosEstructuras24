# Comparisons:
#   Equal: ==
#   Not Equal: !=
#   Greather than: >
#   Less than: <
#   Greather or equal: >=
#   less or equal: <=
#   Object Identity: is

if True:
    print('Conditional is true')

language = str(input())

if language == 'python':
    print('language is python')
elif language == 'Java':
    print('language is java')
else:
    print('else')

a = [1,2,3]
b = [1,2,3]

#its false because their id is different 
print(id(a))
print(id(b))
print(a is b)

#they are the same here so it is true 
b = a
print(a is b)

#Its false because the varaible is empty, this applies to lists 
condition = None

if condition:
    print('true')
else:
    print('false')
