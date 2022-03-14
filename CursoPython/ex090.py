aluno = dict()
aluno["nome"] = str(input('Nome: '))
aluno["media"] = float(input(f'Média de {aluno["nome"]}: '))
if aluno["media"] >= 7:
    aluno["situação"] = "Aprovado"
elif aluno["media"] >= 5:
    aluno["situação"] = "Recuperação"
else:
    aluno["situação"] = "Reprovado"
print('-=' * 20)
for a,b in aluno.items():
    print(f'— {a} é igual a {b}')
#print(f'- nome é igual a {aluno["nome"]}')
#print(f'- média é igual a {aluno["media"]}')
#print(f'- situação é igual a {aluno["situação"]}')
