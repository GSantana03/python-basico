import os

def definir_desconto(porcentagem):
    def calcular_desconto(valor):
        return valor - ((valor * porcentagem)/100)
    return calcular_desconto

def tratar_erro(mensagem):
    input(f"{mensagem} Aperte qualquer tecla para continuar ")
    main()

def main():
    os.system("cls")
    try:
        desconto = float(input("Digite a porcentagem de desconto: "))
        valor = float(input("Digite o valor da compra: "))
    except:
        tratar_erro("Os dados informados são inválidos.")
    else:
        calcular_desconto = definir_desconto(desconto)
        print(f"Preço final com desconto: {calcular_desconto(valor)}")

if __name__ == "__main__":
    main()