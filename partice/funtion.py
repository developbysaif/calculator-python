#Function pactice 
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
