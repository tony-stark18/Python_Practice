print(10-2*4)
#Here we will gate 2 as output because it will perform multiplication first
# paranthesis has more precendence than any operators
# Priority oder is 
# 1.Paranthesis
# 2.Exponent
# 3.Unary plus, Uniary Minus, Bitwise NOT (+x,-x,~x)
# 4.Multiplication,Division,Floor Division, Modulus
# 5.
# print(10*2//3)
#When two operators have same precedence , then associativity helps us to determine the value . It is always from left to right(in most of the operators)
# print(2**3**4)
#Exponent operator has right to left associativity
r=float(input('R: '))
h=float(input('H: '))
print('Area:',format((2*3.141*r*h)+(2*3.141*r*r),'.2f'))