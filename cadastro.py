nomes = []
email = []
print('Seja bem-vindo ao programa de cadastro!')
while True:
    nomes.append(str(input(f'Cadastre um nome: ')).capitalize())
    email.append(str(input(f'digite seu email: ')))
    resposta = str(input("Quer continuar? (S/N) ")).upper()
    while resposta not in 'S''N':
        print('\033[31mERRO!!!\033[m')
        resposta = str(input('\033[33mDigite apenas: S ou N :\033[m ').upper())
    if resposta == 'N':
        break
print(f'Ao todo tivemos {len(nomes)} nomes cadastrados.')
for ordem, nome in enumerate(nomes):
    print(f'{ordem + 1}° \033[34m{nome}\033[m.')
for ordem, mail in enumerate(email):
    print(f'{ordem + 1}°email \033[33m{mail}\033[m')
print('Obrigado por utilizar este programa.')
print('Até a próxima!')


