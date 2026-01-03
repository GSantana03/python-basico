import os

#achei que para valores de venda faz mais sentido usar float e não inteiro
def converte_strings_para_floats(lista_strings):
    lista_floats = []
    for string in lista_strings:
        lista_floats.append(float(string))
    return lista_floats

calcula_total = lambda numeros: sum(numeros)

def dados_invalidos():
    input("Os dados informado estão inválidos. Aperte qualquer tecla para tentar novamente ")
    main()

def main():
    os.system("cls")
    try:
        vendas = input("Digite os valores das vendas ").split(" ")
        numeros = converte_strings_para_floats(vendas)
    except:
        dados_invalidos()
    else:
        total = calcula_total(numeros)
        print(f"O total das vendas foi: {total:.2f}")

if __name__ == "__main__":
    main()