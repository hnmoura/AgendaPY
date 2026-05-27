
ARQUIVO = "contatos.txt" #Aponta onde as informações serão salvas 

def carregar_contatos(): #Função para carregar os contatos 
    contatos = [] #Função vazia para guardar os contatos a medida em que são criados

    try:
        with open(ARQUIVO, "r", encoding="utf-8") as arquivo:
            linhas = arquivo.readlines()

            for linha in linhas:
                dados = linha.strip().split(";")

                contato = {
                    "nome": dados[0],
                    "telefone": dados[1],
                    "email": dados[2],
                    "endereco": dados[3]
                }

                contatos.append(contato)

    except FileNotFoundError:
        pass

    return contatos

def salvar_contatos(contatos): #Função para salvar  os contatos 
    with open(ARQUIVO, "w", encoding="utf-8") as arquivo:

        for contato in contatos:
            linha = (
                f"{contato['nome']};"
                f"{contato['telefone']};"
                f"{contato['email']};"
                f"{contato['endereco']}\n"
            )

            arquivo.write(linha)


def cadastrar_contato(contatos): # Função para cadastrar os contatos 

    print("\n CADASTRAR CONTATO")

    nome = input("Nome: ")
    telefone = input("Telefone: ")
    email = input("Email: ")
    endereco = input("Endereço: ")

    contato = {
        "nome": nome,
        "telefone": telefone,
        "email": email,
        "endereco": endereco
    }

    contatos.append(contato) #Adiciona os contatos numa lista 

    salvar_contatos(contatos)

    print("Contato cadastrado com sucesso!")

def listar_contatos(contatos): # Função para listar os contatos 

    print("\n LISTA DE CONTATOS")

    if len(contatos) == 0:
        print("Nenhum contato cadastrado.")
        return

    for i, contato in enumerate(contatos): #Os contatos são enumados aqui pra que sejam impressos com um número identificador 

        print(f"\nContato {i + 1}")
        print(f"Nome: {contato['nome']}")
        print(f"Telefone: {contato['telefone']}")
        print(f"Email: {contato['email']}")
        print(f"Endereço: {contato['endereco']}")


def buscar_contato(contatos): #Função para listar os contatos 

    print("\n BUSCAR CONTATO")

    nome_busca = input("Digite o nome: ")

    encontrado = False

    for contato in contatos:

        if contato["nome"]() == nome_busca():

            print("\nContato encontrado:")
            print(f"Nome: {contato['nome']}")
            print(f"Telefone: {contato['telefone']}")
            print(f"Email: {contato['email']}")
            print(f"Endereço: {contato['endereco']}")

            encontrado = True

    if not encontrado:
        print("Contato não encontrado.")

def editar_contato(contatos): #Função para editar os contatos 

    print("\n EDITAR CONTATO")

    nome_busca = input("Digite o nome do contato: ")

    for contato in contatos:

        if contato["nome"]() == nome_busca():

            print("Digite os novos dados:")

            contato["nome"] = input("Novo nome: ")
            contato["telefone"] = input("Novo telefone: ")
            contato["email"] = input("Novo email: ")
            contato["endereco"] = input("Novo endereço: ")

            salvar_contatos(contatos)

            print("Contato atualizado com sucesso!")
            return

    print("Contato não encontrado.")

def excluir_contato(contatos): #Função para excluir os contatos 

    print("\nEXCLUIR CONTATO")

    nome_busca = input("Digite o nome do contato: ")

    for contato in contatos:

        if contato["nome"]() == nome_busca():

            contatos.remove(contato)

            salvar_contatos(contatos)

            print("Contato removido com sucesso!")
            return

    print("Contato não encontrado.")

def menu():

    contatos = carregar_contatos() #Os contatos são carregados aqui e enquanto o usuário digitar opções válidas as informação são exibidas 

    while True:

        print("\nAGENDA TELEFÔNICA")
        print("1 - Cadastrar contato")
        print("2 - Listar contatos")
        print("3 - Buscar contato")
        print("4 - Editar contato")
        print("5 - Excluir contato")
        print("0 - Fechar")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_contato(contatos)

        elif opcao == "2":
            listar_contatos(contatos)

        elif opcao == "3":
            buscar_contato(contatos)

        elif opcao == "4":
            editar_contato(contatos)

        elif opcao == "5":
            excluir_contato(contatos)

        elif opcao == "0":
            break

        else:
            print("Opção inválida!")

menu()