import random
import os

NUMERO_MINIMO = 1
NUMERO_MAXIMO = 100

gerar_numero = lambda min, max: random.randrange(min, max + 1, 1)

def verificar_numero(numero_escolhido, numero_cpu):
    if numero_cpu == numero_escolhido:
        print(f"\nParabéns! Você acertou o número {numero_escolhido}")
    elif numero_cpu < numero_escolhido:
        numero_escolhido = receber_entrada("\nMuito alto! Tente novamente: ") 
        verificar_numero(numero_escolhido, numero_cpu)
    else:
        numero_escolhido = receber_entrada("\nMuito baixo! Tente novamente: ")
        verificar_numero(numero_escolhido, numero_cpu)

def receber_entrada(mensagem):
    try:
        numero_escolhido = int(input(f"{mensagem}"))
    except:
        return receber_entrada(f"Entrada inválida: invalid literal for int() with base 10: 'abc12. Digite um número entre {NUMERO_MINIMO} e {NUMERO_MAXIMO}: ")
    else:
        if numero_escolhido >= NUMERO_MINIMO and numero_escolhido <= NUMERO_MAXIMO:
            return numero_escolhido
        else:
            return receber_entrada(f"Entrada inválida: Número fora do intervalo! Digite um número entre {NUMERO_MINIMO} e {NUMERO_MAXIMO}: ")

def main():
    os.system("cls")
    numero_escolhido = receber_entrada(f"Tente adivinhar o número ({NUMERO_MINIMO}-{NUMERO_MAXIMO}): ")
    numero_cpu = gerar_numero(NUMERO_MINIMO, NUMERO_MAXIMO)
    verificar_numero(numero_escolhido, numero_cpu)

if __name__ == "__main__":
    main()