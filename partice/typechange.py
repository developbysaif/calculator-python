a ="1"
b ="2"
c = "3"

num = int(a) + int(b) + int(c)
print(num)

str = "15"
a = 1
str_num = int(str)+a
print (str_num)

a = input("Enter a number: ")
b = input("Enter another number: ")
num = str(a) + str(b)
print("The sum of the two numbers is: ", num)
count = 10 

while (count >0):
    print (count)

    count = count - 1
    if (count ==3):
        continue

for i in range(12):
    if (i == 10):
        break
    print("9 X", i+1, "=", 9*(i+1))


print ("loop ko chodkar nikal jau")

for i in range(12):
    if (i == 10):
        continue
    print("9 X", i+1, "=", 9*(i+1))


