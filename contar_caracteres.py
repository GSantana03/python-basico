#Utilizando len
calcula_caracteres_len = lambda palavra: len(palavra)

#Sem utilizar len
def calcula_caracteres_for(palavra):
    quantidade_caracteres = 0
    for _ in palavra:
        quantidade_caracteres+=1
    return quantidade_caracteres

palavra = input("Digite uma palavra: ")
quantidade_caracteres = calcula_caracteres_for(palavra)
print(f"Sem usar len: Essa palavra tem {quantidade_caracteres} caracteres")

quantidade_caracteres = calcula_caracteres_len(palavra)
print(f"Utilizando len: Essa palavra tem {quantidade_caracteres} caracteres")