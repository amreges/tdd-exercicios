def inss(salario, inss):
    soma = salario-salario * inss / 100
    return soma

def vt(salario, vt):
    soma = salario-salario * vt / 100
    return soma

def plano_saude(valor_total, descon_ps):
    soma = valor_total-valor_total * descon_ps / 100
    return soma

salario = int (input('Digite seu salario: '))
desconto = inss(1000, 9)
desconto2 = vt(desconto, 3)
desconto3 = plano_saude(15, 347)
print ('O salario líquido é:')
print(desconto2 - desconto3)


