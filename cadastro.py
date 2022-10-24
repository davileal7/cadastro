nomes = []
print('Seja bem-vindo ao programa de cadastro!')
while True:
    nomes.append(str(input(f'Cadastre um nome: ')))
    resposta = str(input("Quer continuar? (S/N) ")).upper()
    if resposta == 'N':
        break
for nome, ordem in enumerate(nomes):
    print(f'{ordem} é o {nome + 1}° nome.')
print(f'Ao todo tivemos {len(nomes)} nomes cadastrados.')
print('Obrigado por utilizar este programa.')
print('Até a próxima!')
