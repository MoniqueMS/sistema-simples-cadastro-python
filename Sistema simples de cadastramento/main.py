print("\n--------------------------------------------------")
print("- Sistema simples para cadastramento de usuários -")
print("--------------------------------------------------")

usuarios = []

while True:
    print("\n-------------------")
    print("- Lista de opções -")
    print("-------------------")
    print("\n1. Cadastrar")
    print("2. Listar")
    print("3. Excluir")
    print("4. Sair")

    opcao = input("\nEscolha: ")

    if opcao == "1":
        print("\n------------")
        print("- Cadastro -")
        print("------------")
        nome = input("\nNome: ")
        idade = input("Idade: ")

        usuario = {
            "nome": nome,
            "idade": idade
        }

        usuarios.append(usuario)
        print("Usuário cadastrado.")

    elif opcao == "2":
        print("\n---------------------")
        print("- Lista de cadastro -")
        print("---------------------\n")
        for i, u in enumerate(usuarios):
            print(f"{i} - Nome: {u['nome']} | Idade: {u['idade']}")

        input("\nPressione ENTER para voltar ao menu...")

    elif opcao == "3":
        print("\n-------------------")
        print("- Excluir usuário -")
        print("-------------------\n")

        if len(usuario) == 0:
            print("Nenhum usuário foi cadastrado ainda.")
        else:
            for i, u in enumerate(usuarios):
                print(f"{i} - {u['nome']} ({u['idade']})")

            try:
                indice = int(input("\nDigite o número do usuário: "))

                if 0 <= indice < len(usuario):
                    removido = usuarios.pop(indice)
                    print(f"\nUsuário {removido['nome']} removido!")
                else:
                    print("índice inválido.")
            except ValueError:
                print("Digite um número válido.")

    elif opcao == "4":
        break

    else:
        print("\nOpção inválida, tente novamente.")