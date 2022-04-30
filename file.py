# args kwargs
def sum(a, b,c):
    return a+b+c
d = {
    'a':10,
    'b':20,
    'c':30
}
# a=10,b=20,c=30
print(sum(**d))


