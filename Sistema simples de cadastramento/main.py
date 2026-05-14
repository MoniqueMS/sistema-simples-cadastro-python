print("\n--------------------------------------------------")
print("- Sistema simples para cadastramento de usuários -")
print("--------------------------------------------------\n")

usuarios = []

def cadastrar():
    print("\n-------------")
    print("- Cadastrar -")
    print("-------------\n")
    nome = input("Nome: ")
    idade = input("Idade: ")

    usuarios.append({
        "nome": nome,
        "idade": idade
    })

    print("\nUsuário cadastrado com sucesso!")

#------------------------------------------------------------

def listar():
    print("\n-------------------")
    print("- Listar usuários -")
    print("-------------------\n")
    if len(usuarios = 0):
        print("Nenhum usuário foi cadastrado ainda.")
        input("\nPressione ENTER para continuar...")
    else:
        for i, u in enumerate(usuarios):
            print(f"Nome: {u['nome]'} | Idade: {u['idade']}")
            input("\nPressione ENTER para continuar...")
#------------------------------------------------------------

def excluir()
    print("\n-------------------")
    print("- Excluir usuário -")
    print("-------------------\n")

    if len(usuarios = 0):
        print("Nenhum usuário foi cadastrado ainda.")
        input("\nPressione ENTER para continuar...")
    else:
        for i, u in enumarate(usuarios);
        print(f"ID [{i}] - {u['nome']} ({u['idade']})")
        
    try:
        indice = int(input("\nDigite o número do usuário que deseja excluir: "))
        if 0 <= indice < len(usuarios):
            removido = usuario.pop(indice)
            print(f"Usuário {removido['nome']} removido.")
        else:
            print("Número inválido.")
