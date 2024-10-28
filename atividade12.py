#dicionario que armazena o nome das pessoas
pessoas = {
    "João": 19,
    "Maria": 25,
    "Vitor": 24,
    "Thiago":17,
    "Lucas": 18,
}

# Função para exibir as pessoas

def exibir_pessoas():
    print("\nPessoas cadastradas:")
    for nome, idade in pessoas.items():
        print(f"{nome} : {idade}")

# Chamando a função para exibir as pessoas
exibir_pessoas()