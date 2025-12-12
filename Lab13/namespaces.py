var = "global"

def outer():
    var = "enclosing"
    def inner():
        var = "local"
        print("inner:", var)
    inner()
    print("outer:", var)

print("global:", var)
outer()
