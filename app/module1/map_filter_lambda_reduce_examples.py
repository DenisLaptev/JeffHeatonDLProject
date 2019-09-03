from functools import reduce


# functions
def say_hello(speaker, person_to_greet, greeting="Hello"):
    print(f'{greeting} {person_to_greet}, this is {speaker}.')


say_hello('Jeff', "John")
say_hello('Jeff', "John", "Goodbye")
say_hello(speaker='Jeff', person_to_greet="John", greeting="Goodbye")

print('-----------------------------------------')


# function that trims white space from a string and capitalizes the first letter
def process_string(str):
    t = str.strip()
    return t[0].upper() + t[1:]


str = process_string("  hello  ")
print(f'"{str}"')

print('-----------------------------------------')

# map
# The map function takes a list and applies a function to each member of the list
# and returns a second list that is the same size as the first.
l = ['   apple  ', 'pear ', 'orange', 'pine apple  ']
l2 = list(map(process_string, l))
print(l2)

# comprehension
# The following comprehension accomplishes the same task as the previous call to map.
l = ['   apple  ', 'pear ', 'orange', 'pine apple  ']
l2 = [process_string(x) for x in l]
print(l2)

print('-----------------------------------------')


# filter
# While a map function always creates a new list of the same size as the original,
# the filter function creates a potentially smaller list.

def greater_than_five(x):
    return x > 5


l = [1, 10, 20, 3, -2, 0]
l2 = list(filter(greater_than_five, l))
print(l2)

print('-----------------------------------------')

# lambda
# A lambda is essentially an unnamed function.

l = [1, 10, 20, 3, -2, 0]
l2 = list(filter(lambda x: x > 5, l))
print(l2)

print('-----------------------------------------')

# reduce
# Like filter and map the reduce function also works on a list.
# However, the result of the reduce is a single value.

# Consider if you wanted to sum the values of a list.
# The sum is implemented by a lambda.
l = [1, 10, 20, 3, -2, 0]
result = reduce(lambda x, y: x + y, l)
print(result)
