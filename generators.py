def count(to):
    for i in range(to):
        yield i
data = count(10)
print(data)
for i in data:
    print(i)
for i in data:
    print("loop is working ")
    print(i)

    
