'''A'''
'''1'''
print('\nA)\n\n1: Hello World!')
print('\n----------------------------------------------------------------------------------\n')

'''2'''
print('2:' '\n a.',10,'\n b.',10.3456,'\n c.',3<4,'\n d.',3>4,'\n e. "valor"')
print('\n----------------------------------------------------------------------------------')

'''B'''

'''1'''

base = int(input('\nB)\n\n1:\nQual a base?\n'))
altura = int(input('Qual a altura?\n'))

print('Área do Retangulo: ',base*altura)
print('\n----------------------------------------------------------------------------------')

'''2'''
municipio = input('\n2:\nQual o município?\n')

eleitores = int(input('Qual o total de eleitores?\n'))

validos = int(input('Quantos votos foram válidos?\n'))

nulos = int(input('Quantos foram nulos?\n'))

brancos = int(input('Quantos foram brancos?\n'))

if validos+nulos+brancos < eleitores:

  porvalidos = (100*validos)/eleitores

  pornulos = (100*nulos)/eleitores

  porbrancos = (100*brancos)/eleitores

  nvotantes = eleitores - validos - nulos - brancos

  pornvotantes = (100*nvotantes)/eleitores

  print('\nResultado:\nMunicípio: ', municipio, '\nEleitores: ', eleitores,           '\nVálidos: ', porvalidos, '%\nNulos: ', pornulos, '%\nBrancos: ', porbrancos,       '%\nNão Votantes: ', pornvotantes, '%')
else:

  print('Dados inválidos\n')
  print('\n----------------------------------------------------------------------------------')
  '''3'''

tipoDeCombustivel = input("\n3:\nQual o combustível? Responda A para Álcool ou G para Gasolina.\n")

litros = int(input('Quantos litros?\n'))


if tipoDeCombustivel.lower() == 'g' :
  if litros <= 20:
    preco = litros*6.08
    precoFinal = preco*97/100
    print('Preço a ser pago: R$',precoFinal)
    
  else:
    preco = litros*6.08
    precoFinal = preco*95/100
    print('Preço a ser pago: R$',precoFinal)

elif tipoDeCombustivel.lower() == 'a':
  if litros <= 20:
    preco = litros*4.65
    precoFinal = preco*97/100
    print('Preço a ser pago: R$',precoFinal)
    
  else:
    preco = litros*4.65
    precoFinal = preco*95/100
    print('Preço a ser pago: R$',precoFinal)
else:
  print('Opção inválida')
    
 