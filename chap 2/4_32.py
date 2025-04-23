LIMIT = 1000
a = 0
b = 1
print("0; 1", end="; ")
while True:
    a = a + b
    if a >= LIMIT: break
    print(a, end="; ")

    b = a + b
    if b >= LIMIT: break
    print(b, end="; ")