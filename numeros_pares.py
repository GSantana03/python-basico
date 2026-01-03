import os

def converter_strings_para_inteiros(lista_strings):
    lista_inteiros = []
    for string in lista_strings:
        lista_inteiros.append(int(string))
    return lista_inteiros

verificar_par = lambda numero: numero % 2 == 0

filtrar_pares = lambda numeros: list(filter(verificar_par, numeros))

converter_lista_para_string = lambda lista, separador: separador.join( str(item) for item in lista )

def dados_invalidos():
    input("Dados inválidos. Aperte qualquer tecla para tentar novamente ")
    main()

def main():
    os.system("cls")
    try:
        valores_informados = input("Digite os números separados por espaço: ").split(" ")
        numeros = converter_strings_para_inteiros(valores_informados)
    except:
        dados_invalidos()
    else:
        pares = converter_lista_para_string(filtrar_pares(numeros), " ") 
        print(f"Números pares: {pares}")
    
if __name__ == "__main__":
    main()