def voto(ano):
    from datetime import datetime
    anoatual = datetime.now().year
    if ano > anoatual:
        return('Erro! Ano de nascimento digitado é maior que o ano atual')
    elif anoatual - ano < 18:
        return(f'Com {anoatual - ano} anos: NÃO VOTA')
    elif 65 > anoatual - ano >= 18:
        return(f'Com {anoatual - ano} anos: VOTO OBRIGATÓRIO')
    elif anoatual - ano >= 65:
        return(f'Com {anoatual - ano} anos: VOTO OPCIONAL')


ano = int(input('Em que ano você nasceu? '))
print(voto(ano))
