nomes = ['Maria', 'Helena', 'Pedro']
nome1, nome2 = ['Maria', 'Helena', 'Pedro'] # ValueError: too many values to unpack
nome1, nome2, nome3, nome4 = ['Maria', 'Helena', 'Pedro'] # ValueError: not enough values to unpack
print(nome2)

nome1, *rest = ['Maria', 'Helena', 'Pedro']

# a variavel rest agora tem o restante da lista que sobrou
# se não for usar a rest, coloco um _

_, nome2, _, *_ = ['Maria', 'Helena', 'Pedro']