numeros = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez',
           'Onze','Doze','Treze','Quartoze','Quinze','Dezesseis', 'Dezessete', 'Dezoito','Dezenove','Vinte')
teste = int(input('Digite um número entre 0 e 20: '))
while teste > 20 or teste < 0:
    teste = int(input('Tente novamente. Digite um número entre 0 e 20: '))
print(f'Você digitou o número {numeros[teste]}.')
