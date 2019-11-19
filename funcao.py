def imprimir_dados(nome, idade=None):
    if idade is not None:
      print("nome: {}, idade: {}". format(nome, idade))
    else:
      print("nome: {}". format(nome))

#imprimir_dados('Amanda', 24)

def somar_numeros(n1, n2):
    soma = n1 + n2
    return soma

resultado = somar_numeros(10, 20)
#print(resultado)

def titulos_copa_mundo(pais, *args):
    print('O país {}'.format(pais))
    print('Ganhou a copa do mundo nos anos: ')
    for titulo in args:
        print(titulo)

titulos_copa_mundo('Brasil', '1990', '1994', '2002')
