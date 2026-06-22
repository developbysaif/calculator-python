# a ="1"
# b ="2"
# c = "3"

# num = int(a) + int(b) + int(c)
# print(num)

# str = "15"
# a = 1
# str_num = int(str)+a
# print (str_num)

# a = input("Enter a number: ")
# b = input("Enter another number: ")
# num = str(a) + str(b)
# print("The sum of the two numbers is: ", num)
# count = 10 

# while (count >0):
#     print (count)

#     count = count - 1
#     if (count ==3):
#         continue

# for i in range(12):
#     if (i == 10):
#         break
#     print("9 X", i+1, "=", 9*(i+1))


# print ("loop ko chodkar nikal jau")

# for i in range(12):
#     if (i == 10):
#         continue
#     print("9 X", i+1, "=", 9*(i+1))

# Function pactice 
# a = int(input("Enter a number: "))
# b = int(input("Enter another number: "))

# gemean = (a*b)/(a +b)

# print ("The geometric mean of the two numbers is: ", gemean)
# print ("The geometric mean of the two numbers is: ", (a*b)/(a +b))
# a = int(input("Enter a number: "))
# b = int(input("Enter another number: "))
# def geometric_mean(a, b):
#     return (a * b) / (a + b)
# print ("The geometric mean of the two numbers is: ", geometric_mean(a, b))

# def isgreater (a, b):
#     if a > b:
#         return True
#     else:
#         return False

# num = int(input("Enter a number: "))
# def even_odd(num):
#     if num % 2 == 0:
#         return "Even"
#     else:
#         return "Odd"

# print(even_odd(num))

# def square(num):
#     return num * num

# print(square(num))

# argument practice
#  there are four type of aregument in python 
# default argument, 
# keyword argument, 
# positional argument, 
# variable length argument

# default argument
def average (a = 6, b=5):
    print("The average of the two numbers is: ", (a + b) / 2)


# average()
# average(10, 20)# priority 

#keyword argument
def average(a, b , c=1):
    print("The average of the two numbers is: ", (a + b + c) / 2)


average(b=10, a=20) # keyword argument

def average (*number):
    sum =0
    for i in number:
        sum += i
    print("The average is: ", sum / len(number))


average(10, 20, 30) # variable length argument

def name (**name):
    print("My name is: ", name["first"], name["last"])


name(first="John", last="Doe") # keyword argument with variable length argument


tup =(1, 2, 3, 4, 5)
# tup[0]=90
print(tup[0] , type(tup)) # get the first element of the tuple

# tuple methode in python
tup =(1, 2, 3,3,3, 4, 5)
tup.index(2) # get the index of the element 2 in the tuple
tup.count(3) # get the count of the element 3 in the tuple
tup.index(3 , 4 ,5) # get the index of the element 3 in the tuple starting from index 4 to index 5

print = (f"the count of the element 3 in the tuple is: {tup}")

 # doc string in python

 # doc is the string that areuse in sitethe function it will be write inthe funtion eect after the function declaration and before the function body
def average(a , b):
    """This function takes two numbers as input and returns their average."""
    return (a + b) / 2
print(average.__doc__) # get the doc string of the function average
 
# zen of python 
import this # it will print the zen of python

#pep 8 is the style guide for python code it will tell you how to write the code in python

#recurions in python 

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


print(5 * factorial(4)) # calculate the factorial of 5

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(10)) # calculate the 10th Fibonacci number
