def add_everything_up(a, b):
    if type(a) != type(b):
        return str(a) + str(b)
    try:
        result = a + b
        return result
    except TypeError:
        print(f"{type(a).__name__} and {type(b).__name__}")

print(add_everything_up(153, 153))
print(add_everything_up("Hello, ", "world!"))
print(add_everything_up(5, "test"))

