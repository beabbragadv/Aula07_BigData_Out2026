total = 0
quantidade = 0

resposta = 'S'
while resposta == 'S':
    despesa = float(input('Informe o valor da pessoa: R$ '))

    total = total + despesa
    quantidade = quantidade + 1

    resposta = input('Deseja continuar? [S/N:]').upper()

    print(f'Quantidade de despesas registradas: R$ {quantidade:.2f}')
    print(f'Valor total das despesas: R$ {total:.2f} ')