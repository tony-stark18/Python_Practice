# #Strings are used to store text data
# #These are written in single quote / double qoute and in triple single or double qoute 

# #Assigning variable to a string 
# a="Hello, I am Diptiranjan Sahoo"
# # we can write it this as well
# b='Hello, I am Diptiranjan Sahoo'
# # and like this also
# c='''Hello, I am Diptiranjan Sahoo''' #This is used for multi line string basically

# d='''Hello, I am Diptiranjan Sahoo,
# I love coding'''#Multi line string
# print(a,b,c,d)

# # String as an array

# e="Hello World"
# print(e[0])

# # To get the length of a string
# print(len(e))

# # Slicing of a string 


#Modify a string

# x="Hello World"    #lower case
# print(x.lower())

#Strip Method used to remove white spaces in a string
x="   Hello World"  
print(x.strip())

# replace function is used to replace one or more character in a string

x="Hello World"  
print(x.replace('H','P'))

# Split function splits a string into two short string making an list from where the space is availabe
x = 'Hello World'
y=x.split()
print(y[1])

# + operator is used to concat strings

x="Hello"
y="World"
print(x+y) 



