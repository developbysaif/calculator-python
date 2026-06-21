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

# lists methode  in python
my_list = [1, 2, 3, 4, 5]
my_list.sort(reverse=True)
my_list.reverse() # reverse the list
my_list.append(6)
my_list.insert(3, 4333) # insert 0 at index 0
my_list.index(2) # get the index of the element 2 in the list

print(my_list)

my_list = l
m[0]=0
print(my_list)

k = [1, 2, 3, 4, 5]
l = [6, 7, 8, 9, 10]
m = [1, 2, 3, 4, 5]
k= l + m # concatenate the list k and m
l.extend(m) # extend the list l with the list m
print(l)





