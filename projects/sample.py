a = "Hello"
b = "Hello"
print(id(a))
print(id(b))

c = a
print(id(c))
a = "hello"

print(id(a))
print(id(c))

