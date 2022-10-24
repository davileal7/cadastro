nomes = []
print('Seja bem-vindo ao programa de cadastro!')
while True:
    nomes.append(str(input(f'Cadastre um nome: ')).capitalize())
    resposta = str(input("Quer continuar? (S/N) ")).upper()
    while resposta not in 'S''N':
        print('\033[31mERRO!!!\033[m')
        resposta = str(input('\033[33mDigite apenas: S ou N :\033[m ').upper())
    if resposta == 'N':
        break
print(f'Ao todo tivemos {len(nomes)} nomes cadastrados.')
for ordem, nome in enumerate(nomes):
    print(f'\033[34m{nome}\033[m é o {ordem + 1}° nome.')
print('Obrigado por utilizar este programa.')
print('Até a próxima!')
