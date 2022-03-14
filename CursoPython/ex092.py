from datetime import datetime
pessoa = dict()
pessoa["nome"] = str(input('Nome: '))
nascimento = int(input('Ano de Nascimento: '))
pessoa["idade"] = datetime.now().year - nascimento
ctps = int(input('Carteira de Trabalho (0 não tem): '))
if ctps == 0:
    pessoa["ctps"] = ctps
    print('-=' * 30)
else:
    pessoa["ctps"] = ctps
    pessoa["contratação"] = int(input('Ano de Contratação: '))
    pessoa["salário"] = int(input('Salário: R$'))
    pessoa["aposentadoria"] = pessoa["contratação"] + 30 - nascimento
    print('-=' * 30)
for i, v in pessoa.items():
    print(f'  — {i} tem o valor {v}')
