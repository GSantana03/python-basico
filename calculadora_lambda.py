import os

somar = lambda parcela1, parcela2 : parcela1 + parcela2
subtrair = lambda minuendo, subtraendo : minuendo - subtraendo
multiplicar = lambda fator, multiplicador : fator * multiplicador
dividir = lambda dividendo, divisor : dividendo / divisor if divisor != 0 else tratar_erro("Não é possível realizar divisão por zero.")

def calcular_operacao(numero1, numero2, operacao):
    match operacao:
        case "+":
            return somar(numero1, numero2)
        case "-":
            return subtrair(numero1, numero2)
        case "*":
            return multiplicar(numero1, numero2)
        case "/":
            return dividir(numero1, numero2)
        case _:
            tratar_erro("Operação escolhida não é válida.")

def tratar_erro(mensagem):
    input(f"{mensagem} Aperte qualquer tecla para continuar ")
    main()

def main():
    os.system("cls")
    try:
        numero1 = float(input("Digite o primeiro número: "))
        numero2 = float(input("Digite o segundo número: "))
    except:
        tratar_erro("O valor informado não é válido.")
    else:
        operacao = input("Escolha a operação (| + | - | * | / |): ")
        resultado = calcular_operacao(numero1, numero2, operacao)
        if resultado != None: print(f"O resultado é: {resultado}")

if __name__ == "__main__":
    main()