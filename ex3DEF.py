def calculo_de_venda (valor, tipo):
    if tipo == 1:
        conta = valor * 0.70
    elif tipo == 2:
        conta = valor * 0.80
    else:
        conta = valor
    return conta

try:
    v = float(input('Informe o valor da compra: R$'))
    print('Tipos de clientes: 1 - Funcionário | 2 - Cliente VIP | 3 - Cliente')
    tipo = float(input('Digite o código correspondente ao tipo de cliente:'))

    if tipo == 3:
        print('O valor do produto é: R$', v)
        print('Não fique sem desconto! Faça o cartão da loja e ganhe descontos imperdíveis de até 20%!!')

    else:
        x = calculo_de_venda (v, tipo)
        print('O valor do(s) produtos com desconto é: R$', x)

except:
    print("ERRO!!! Digite apenas números válidos.")
        
