# global
x = "global"


def outer():
    # global x
    x = "local in func outer"

    def inner():
        # nonlocal x
        # global x
        x = "nonlocal in inner"
        print("inner:", x)
    inner()
    print("outer:", x)


outer()
# inner() # Error: NameError: name 'inner' is not defined
print("global x:", x)
