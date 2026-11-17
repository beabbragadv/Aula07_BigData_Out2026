meta = 2000
resposta = 'S'
while resposta == "S" :
    vendas = float(input('Informe o valor vendido: R$ '))

    atingimento = (vendas / meta) * 100

    print(f'\nVendeu R$: {vendas:.2f}')
    print(f'Meta atingida: {atingimento:.2f}')

    resposta = input('\nDeseja cadastrar outro vendedor? [S/N:]').upper()