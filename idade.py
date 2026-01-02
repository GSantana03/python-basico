print('hello wolrd')

def calcula_idade(ano_nascimento , ano_atual):
    return ano_atual - ano_nascimento

def pede_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print('Entrada invalida , por favor digite apenas numeros inteiros')

nascimento= pede_int('Digite o ano que você nasceu :')
atual = pede_int('Digite o ano atual :')
idade= calcula_idade (nascimento,atual)
print(f'Você tem {idade} anos de idade')