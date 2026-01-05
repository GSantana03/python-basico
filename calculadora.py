import os

somar = lambda numero1, numero2 : numero1 + numero2
subtrair = lambda numero1, numero2: numero1 - numero2
multiplicar = lambda numero1, numero2: numero1 * numero2
dividir = lambda numero1, numero2: numero1/numero2 if numero2 != 0 else tratar_erro("Erro: Divisão por zero não é permitida.")

def calcular_operacao(numero1, numero2, operacao):
    match operacao:
        case "+":
            return somar(numero1, numero2)
        case "-":
            return subtrair(numero1, numero2)
        case "*":
            return multiplicar(numero1, numero2)
        case "/":
            return  dividir(numero1, numero2)
        case _:
            tratar_erro("Opção Inválida.")

def tratar_erro(mensagem):
    input(f"{mensagem} Aperte qualquer tecla para tentar novamente. ")
    main()

def executar_calculo():
    try:
        numero1 = float(input("Digite o primeiro número: "))
        operacao = input("Digite a operação (+, -, *, /): ")
        numero2 = float(input("Digite o segundo número: "))
        return calcular_operacao(numero1, numero2, operacao)
    except:
        tratar_erro("Erro: Entrada inválida. Digite apenas números.")

def mostrar_resultado():
    resultado = executar_calculo()
    if resultado != None:
        print(f"Resultado: {resultado}")

def main():
    os.system("cls")
    mostrar_resultado()

if __name__ == "__main__":
    main()