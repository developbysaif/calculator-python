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

num = int(input("Enter a number: "))
def even_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

print(even_odd(num))

def square(num):
    return num * num

print(square(num))

