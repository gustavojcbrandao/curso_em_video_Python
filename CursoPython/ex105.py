def notas(* n, sit=False):
    """
    —> Função para analisar as notas e situações de vários alunos.
    :param n: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma
    """
    soma = total = maior = menor = 0
    situacao = ''
    print('—'*30)
    for c in range(0, len(n)):
        total += 1
        soma += n[c]
        if c == 0:
            maior = menor = n[c]
        else:
            if n[c] > maior:
                maior = n[c]
            if n[c] < menor:
                menor = n[c]
    media = soma/len(n)
    if media >= 7:
        situacao = 'BOA'
    elif 7 > media >= 5:
        situacao = 'REGULAR'
    elif media < 5:
        situacao = 'RUIM'
    if sit:
        return{'total': total, 'maior': maior, 'menor': menor, 'media': media, 'situação': situacao}
    else:
        return{'total': total, 'maior': maior, 'menor': menor, 'media': media}


resp = notas(5.5, 2.5, 1.5, sit=True)
print(resp)
