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

    # List par loop
fruits = ["apple", "banana", "mango"]
for fruit in fruits:
    print(fruit)
# Output: apple, banana, mango

# Range ke saath
for i in range(5):
    print(i)
# Output: 0 1 2 3 4

# String par loop
for char in "hello":
    print(char)
# Output: h e l l o

# Dictionary par loop
person = {"name": "Ali", "age": 25}
for key, value in person.items():
    print(key, ":", value)
# Output: name : Ali,  age : 25

# Basic while loop
count = 0
while count < 5:
    print(count)
    count += 1
# Output: 0 1 2 3 4

# User input ke saath
while True:
    name = input("Enter name (q to quit): ")
    if name == "q":
        break
    print("Hello", name)

  #Loop control statement 
  #Break statement: Loop ko turant rok deta hai.
  #Continue statement: Loop ke current iteration ko skip kar deta hai aur next iteration par ch 
#ala jata hai.
#Pass statement: Loop ke andar koi code nahi likhna hai to pass statement ka use karte hain.
# break example
for i in range(10):
    if i == 5:
        break       # 5 par ruk jayega
    print(i)
# Output: 0 1 2 3 4

# continue example
for i in range(6):
    if i == 3:
        continue    # 3 ko skip karega
    print(i)
# Output: 0 1 2 4 5

# pass example
for i in range(3):
    pass            # abhi kuch nahi karna

# usefull loop tricks
# enumerate - index aur value dono
for i, val in enumerate(["a", "b", "c"]):
    print(i, val)
# Output: 0 a, 1 b, 2 c

# zip - do lists saath mein
names = ["Ali", "Sara"]
ages  = [25, 30]
for name, age in zip(names, ages):
    print(name, age)
# Output: Ali 25, Sara 30

# nested loop - loop ke andar loop
for i in range(3):
    for j in range(3):
        print(i, j)

# list comprehension - ek line mein loop
squares = [x**2 for x in range(5)]
print(squares)
# Output: [0, 1, 4, 9, 16]