my_string = "Hello, World!"
print(my_string[0]) 
print(my_string[7]) 


my_string = "Hello, World!"
print(my_string[0:5]) 
print(my_string[7:]) 
print(my_string[:5]) 
print(my_string[-6:]) 



string1 = "Hello"
string2 = "World"
concatenated_string = string1 + ' ' + string2
print(concatenated_string) 




my_string = "Hello, World!"
length = len(my_string)
print(length) 



text = "Hello World"
print(text.lower())  



text = "Hello World"
print(text.upper())  



text = "   Hello World   "
print(text.strip())  


text = "Hello World"
print(text.split())  

text = "apple,banana,cherry"
print(text.split(","))  



text = "Hello World"
print(text.replace("World", "Python"))  



text = "Hello World"
print(text.find("World"))  
print(text.find("Python"))  



my_string = "Hello, World!"
print(my_string.lower()) 
print(my_string.upper()) 
print(my_string.strip()) 
print(my_string.split(',')) 
print(my_string.replace('Hello', 'Hi'))
print(my_string.find('World'))




name = "Ranadheer"
age = 19
formatted_string = "My name is %s and I am %d years old." % (name, age)
print(formatted_string)



name = "Alice"
age = 25
formatted_string = "My name is {} and I am {} years old.".format(name, age)
print(formatted_string)



name = "John"
age = 25
message = f"Hello, my name is {name} and I am {age} years old."
print(message) 



num = 42
result = f"The answer is {num * 2}"
print(result)




s = “Hello, World!”
for char in s:
    print(char)



s = 'Hello, World!'
i = 0
while i < len(s):
    print(s[i])
    i += 1




s= 'reehdanar'
print(s[::-1])



s = “Hello, World!”
char = ‘o’
index = s.index(char)
print(“The first occurrence of”, char, “is at index”, index)







