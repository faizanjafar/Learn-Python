def double_args(fuc):
    def wapper(a,b):
        return fuc(2*a , 2*b)
    return wapper


def mul(a,b):
    return a * b

new_mul = double_args(mul)
print(new_mul(1,5))