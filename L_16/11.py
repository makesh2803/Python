### This way function will receive a tuple, and can access the items accordingly
def my_function(*kids):
    print("The youngest child is " + kids[2])
my_function("Emil", "Tobias", "Linus")