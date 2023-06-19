def my_function(*args, **kwargs):
    for arg in args:
        print("this is from args : " + str(arg))

    for key, value in kwargs.items():
        print("this is from kwargs : "  + key, value)

def generate_numbers():
    for i in range(1, 6):
        yield i

# Using the generator function
numbers = generate_numbers()
print(type(numbers))
# Iterating over the generator
for i in range(5):
    print(next(numbers))