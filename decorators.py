
def decorator_func(url):
    def wrapper_func(func):
        def dec_func(*args, **kwargs):
            print("calling a function", func.__name__)
            print("url", url)
            func(*args, **kwargs)
        return dec_func
    return wrapper_func


@decorator_func(url="https://google.com")
def sayHello(name):
    print("Hello ",name)

sayHello("Ali")
sayHello("Moin")
sayHello("Ahmad")
