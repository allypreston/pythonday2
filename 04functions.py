# functions
# run blocks of code when called
# should be unitary / small
# they can take in arguments
#
# function is like a machine
# it can take in inputs
# it can perform actions
# it outputs different objects
#
# syntax of a function
# def function_name(arguments):
#   runs block of code
#   return code
#
# a function needs to be called to run it's code
#
# good practices
# - functions should be small
# - arguments should have good names
# - functions should be used to keep your code DRY
#   - DRY = don't repeat yourself
# - functions should return NOT print
def say_hello():
    print('Hello there')

say_hello()

def full_name(f_name, l_name):
    full_name_var = f_name + ' ' + l_name
    return full_name_var


print(full_name('Ally', 'Preston'))