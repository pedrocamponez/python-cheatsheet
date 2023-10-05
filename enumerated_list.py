lista = ['Maria', 'Helena', 'Pedro']
lista.append('João')

enumerated_list = enumerate(lista)

for item in enumerated_list:
    print(item)

# After enumerating a list and using it (as in line 4), it become empty

print(enumerated_list)

for item in enumerated_list:
    print(item)

# you can change that by changing the type of the enumerated list

enumerated_list = list(enumerate(lista))

# unpacking:
# a for inside the for, but Python does it for us
for index, name in enumerate(lista):
    print(index, name)