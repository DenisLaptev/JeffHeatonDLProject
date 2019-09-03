c = ['a', 'b', 'c', 'd']
print(c)

print('---------------------------------------')

# Iterate over a collection.
for s in c:
    print(s)

print('---------------------------------------')

# Iterate over a collection, and know where your index.  (Python is zero-based!)
for i, c in enumerate(c):
    print(f"{i}:{c}")

print('---------------------------------------')

# Manually add items, lists allow duplicates
c = []
c.append('a')
c.append('b')
c.append('c')
c.append('c')
print(c)

print('---------------------------------------')

# Manually add items, sets do not allow duplicates
# Sets add, lists append.  I find this annoying.
c = set()
c.add('a')
c.add('b')
c.add('c')
c.add('c')
print(c)

print('---------------------------------------')

# Insert
c = ['a', 'b', 'c']
c.insert(0, 'a0')
print(c)

# Remove
c.remove('b')
print(c)

# Remove at index
del c[0]
print(c)

print('---------------------------------------')

# Dictionaries

d = {'name': "Jeff", 'address': "123 Main"}
print(d)
print(d['name'])

if 'name' in d:
    print("Name is defined")

if 'age' in d:
    print("age defined")
else:
    print("age undefined")

print('---------------------------------------')

d = {'name': "Jeff", 'address': "123 Main"}

# All of the keys
print(f"Key: {d.keys()}")

# All of the values
print(f"Values: {d.values()}")

print('---------------------------------------')

# Python list & map structures
customers = [
    {"name": "Jeff & Tracy Heaton", "pets": ["Wynton", "Cricket", "Hickory"]},
    {"name": "John Smith", "pets": ["rover"]},
    {"name": "Jane Doe"}
]

print(customers)

for customer in customers:
    print(f"{customer['name']}:{customer.get('pets', 'no pets')}")

print('---------------------------------------')

a = [1, 2, 3, 4, 5]
b = [5, 4, 3, 2, 1]

print(zip(a, b))

print('---------------------------------------')

a = [1, 2, 3, 4, 5]
b = [5, 4, 3, 2, 1]

print(list(zip(a, b)))

print('---------------------------------------')

a = [1, 2, 3, 4, 5]
b = [5, 4, 3, 2, 1]

for x, y in zip(a, b):
    print(f'{x} - {y}')
    print(f'x+y={x + y}')

print('---------------------------------------')

a = ['one', 'two', 'three', 'four', 'five']
print(enumerate(a))
print(list(enumerate(a)))

print('---------------------------------------')

a = ['one', 'two', 'three', 'four', 'five']
for idx, item in enumerate(a):
    print(f'Index {idx} holds "{item}"')

print('---------------------------------------')

lst = [x * 10 for x in range(10)]
print(lst)

print('---------------------------------------')

text = ['col-zero', 'col-one', 'col-two', 'col-three']
lookup = {key: value for (value, key) in enumerate(text)}
print(lookup)

print('---------------------------------------')

print(f'The index of "col-two" is {lookup["col-two"]}')

print('---------------------------------------')

print(range(10))
print(list(range(10)))
