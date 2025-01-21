### This way function will receive a dictionary, and can access the items accordingly
def my_function(**kid):
    print("His last name is " + kid["lname"])
my_function(fname = "Tobias", lname = "Refsnes")