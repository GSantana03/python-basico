
import re

padrao_cpf = re.compile(r"\d{3}\.\d{3}\.\d{3}-\d{2}")
cpf = input("Digite o CPF: ")

if padrao_cpf.fullmatch(cpf):
    print("CPF valido")
else:
    print("CPF invalido")