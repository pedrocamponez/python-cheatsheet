# Tuple = a list that can't be changed :)

nomes = 'Maria', 'Helena', 'Pedro'
nomes[1] = 'outro' # TypeError: 'tuple' object does not support item assignment
print(nomes)

nomes2 = 'Maria', 'Helena', 'Pedro', 'Carol'
nomes2 = list(nomes2)
nomes2 = tuple(nomes2)