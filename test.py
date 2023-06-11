def my_function(*args, **kwargs):
    for arg in args:
        print("this is from args : " + str(arg))

    for key, value in kwargs.items():
        print("this is from kwargs : "  + key, value)



my_function(path ={"this"})
