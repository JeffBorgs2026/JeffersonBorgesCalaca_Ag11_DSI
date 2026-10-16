# Define o número total de entrevistados que serão consultados na pesquisa (ajuste para 10 se for realizar o teste rápido pedido na atividade)
total_entrevistados = 10  

# Inicializa o contador para armazenar a quantidade de respostas "EXCELENTE" com o valor zero
qtd_excelente = 0

# Inicializa o contador para armazenar a quantidade de respostas "RUIM" com o valor zero
qtd_ruim = 0

# Inicia uma estrutura de repetição (for) que vai iterar do número 1 até o total de entrevistados definido
for i in range(1, total_entrevistados + 1):

    # Exibe no console um cabeçalho indicando o número atual do entrevistado em relação ao total
    print(f"\n--- Entrevistado {i} de {total_entrevistados} ---")

    # Solicita ao usuário que digite o nome do entrevistado atual e armazena na variável 'nome'
    nome = input("Digite o nome: ")

    # Solicita a idade do entrevistado, convertendo o texto digitado em um número inteiro (int)
    idade = int(input("Digite a idade: "))

    # Exibe na tela o menu com as opções de avaliação disponíveis para o atendimento
    print("Opinião sobre o atendimento:")
    print("1: EXCELENTE")
    print("2: BOM")
    print("3: RUIM")

    # Solicita que o usuário digite o número correspondente à opinião e converte para número inteiro
    opiniao = int(input("Digite a opção (1, 2 ou 3): "))

    # Cria uma estrutura de repetição de validação para garantir que o usuário digite apenas 1, 2 ou 3
    while opiniao not in [1, 2, 3]:

        # Avisa que a opção digitada é inválida caso o usuário erre o número
        print("Opção inválida! Digite novamente.")

        # Pede novamente para digitar a opção correta
        opiniao = int(input("Digite a opção (1, 2 ou 3): "))

    # Verifica se a opinião escolhida foi 1 (EXCELENTE) usando uma estrutura de decisão (if)
    if opiniao == 1:

        # Incrementa em 1 a contagem de respostas excelentes
        qtd_excelente += 1

    # Verifica se a opinião escolhida foi 3 (RUIM) usando uma estrutura condicional (elif)
    elif opiniao == 3:

        # Incrementa em 1 a contagem de respostas ruins
        qtd_ruim += 1

# Exibe o título indicando que os resultados finais da pesquisa serão mostrados
print("\n=== Resultado Final da Pesquisa ===")

# Mostra na tela a quantidade total de respostas "EXCELENTE" acumuladas no laço de repetição
print(f"a) Quantidade de respostas 'EXCELENTE': {qtd_excelente}")

# Mostra na tela a quantidade total de respostas "RUIM" acumuladas no laço de repetição
print(f"b) Quantidade de respostas 'RUIM': {qtd_ruim}")