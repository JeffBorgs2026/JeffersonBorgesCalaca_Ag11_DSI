def calcular_media(nota1, nota2):
    soma = nota1 + nota2
    media = soma / 2
    return media

def verificar_status(media):
    if media >= 6.0:
        return "Aprovado"
    else:
        return "Reprovado"

# Entrada de dados
nome_aluno = input("Digite o nome do aluno: ")
nota_um = float(input("Digite a primeira nota: "))
nota_dois = float(input("Digite a segunda nota: "))

# Processamento
media_final = calcular_media(nota_um, nota_dois)
situacao_aluno = verificar_status(media_final)

# Saída de dados
print("Aluno:", nome_aluno)
print("Média:", media_final)
print("Situação:", situacao_aluno)