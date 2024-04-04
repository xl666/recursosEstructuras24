str1 = "   Welcome to Great Learning!   "
print("Original String:", str1)

# Using strip() without specifying chars
str2 = str1.strip()
print("After stripping whitespace:", str2)

# Using strip() with specified chars
str3 = "****Welcome to Great Learning!****"
str4 = str3.strip("*")
print("After stripping '*' characters:", str4)

str5 = "Welcome to Great Learning!99!"
str6 = str5.strip("9!")
print("After stripping '9' and '!' characters:", str6)

str7 = "toWelcome to Great Learning!to"
str8 = str7.strip("to")
print("After stripping 't' and 'o' characters from the beginning and end:", str8)