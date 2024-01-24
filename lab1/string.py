#string literal
x = "HELLO"
print('HELLO')

#assign String to a Variable
x = "HELLO"
print(x)

#Multiline Strings
x = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua. """
print(x)

a = "Hello, World!"
print(a[0])

for x in "banana":
    print(x)

b = "Hello, World!"
print(len(b))

txt = "the best thing in life are free"
print("free" in txt)

txt = "the best thing in life are free"
if "free" in txt:
    print("Yes, 'free' is present")

txt = "the best thing in life are free"
print("free" not in txt)

txt = "the best thing in life are free"
if("expensive" not in txt):
    print("No, 'expensive' is NOT present")

#slicing
x = "Hello, World"
print(x[2:7])

#slice from the start 
x = "Hello, Wolrd"
print(x[:5])

#negative indexing
x = "Hello, World"
print(x[-5:-2])

#upper case
a = "Hello, Wolrd!"
print(a.upper())

#lower case
a = "Hello, World!"
print(a.lower())

#remove whitespace
a = "Hello, World! "
print(a.strip())

#replace string
a = "Hello, World!"
print(a.replace("H", "J"))

#split string 
a = "Hello, World"
print(a.split(","))

#String Concatenation
a = "Hello"
b = "World"
c = a + b
print(c)

a = "Hello"
b = "World"
c = a + " " + b
print(c)

#String Format
age = 18
txt = "My name is Madina, i am {}"
print(txt.format(age))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of {} for {}"
print(myorder.format(quantity, itemno, price))

quantity = 3
itemno = 567
price = 49.95
myrder = "I want to pay {2} dollar for {0} pieces of item {1}"
print(myrder.format(quantity, itemno, price))

txt = "I'am studying in \"KBTU\""
print(txt)