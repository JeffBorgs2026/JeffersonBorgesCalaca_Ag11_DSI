import random

# Listas de apoio para gerar dados fictícios aleatórios
nomes_possiveis = ["Ana", "Bruno", "Carlos", "Diana", "Eduardo", "Fernanda", "Gabriel", "Helena", "Igor", "Jéssica"]

TOTAL_ENTREVISTADOS = 50

qtd_excelente = 0
qtd_ruim = 0

print("--- INÍCIO DA PESQUISA DE OPINIÃO TUDOWEB (MODO AUTOMÁTICO) ---")

for i in range(TOTAL_ENTREVISTADOS):
    # Gerando dados automáticos para simular o usuário
    nome_gerado = random.choice(nomes_possiveis)
    idade_gerada = random.randint(18, 65)
    opiniao_gerada = random.randint(1, 3)  # Sorteia entre 1 (Excelente), 2 (Bom) e 3 (Ruim)

    # Imprimindo a simulação na tela para você ver o que o programa está "digitando"
    print(f"\nEntrevistado {i + 1}:")
    print(f"Digite o nome: {nome_gerado}")
    print(f"Digite a idade: {idade_gerada}")
    print("Opinião sobre o atendimento:")
    print("1 - EXCELENTE")
    print("2 - BOM")
    print("3 - RUIM")
    print(f"Digite o número correspondente à sua opinião: {opiniao_gerada}")

    # Estrutura de decisão para contabilizar as respostas sorteadas
    if opiniao_gerada == 1:
        qtd_excelente += 1
    elif opiniao_gerada == 3:
        qtd_ruim += 1

print("\n--- RESULTADO FINAL DA PESQUISA ---")
print(f"a) Quantidade de respostas 'EXCELENTE': {qtd_excelente}")
print(f"b) Quantidade de respostas 'RUIM': {qtd_ruim}")