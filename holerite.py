
salario = float(input("Insira o valor do seu salário aqui: R$ "))

def inss_calculo(salario, inss):
    return salario * inss

resultado = inss_calculo(salario, 0.09)
print("O desconto do seu INSS é de: ", resultado)

def vt_calculo(salario, vt):
    return salario * vt

resultado_2 = vt_calculo(salario, 0.03)
print("O desconto do seu vale transporte é de: ", resultado_2)

def convenio_calculo(salario, convenio):
    return salario * convenio

resultado_3 = convenio_calculo(salario, 0.15)
print("O desconto do seu convênio é de: ", resultado_3)

def salarioliquido(salario, salarioliquido):
    return salario - salarioliquido

resultado_4 = salarioliquido(salario, (0.03 + 0.09 + 0.15))
print("O valor do seu salário líquido é: ", resultado_4)
