perfil = {}

def cadastrar_usuario():
    Nome = input("Digite seu nome de usuário: ")
    if Nome in perfil:
        print("Usuário já existente, tente outros nomes")
    else:
        Senha = int(input("Crie sua senha: "))
        perfil[Nome] = Senha
        print("Cadastro efetuado com sucesso!")

def login():
    Nome = input("Informe seu nome: ")
    if Nome in perfil:
        Senha = int(input("Informe sua senha: "))
        if perfil[Nome] == Senha:
            print("Login efetuado com sucesso!")
        else:
            print("Esta senha não existe")
    else:
        print("Este usuário não existe")

def menu():
    while True:
        print("[1] Cadastro")
        print("[2] Login")
        print("[3] Sair")
        opcao = input("Digite aqui um dos números acima: ")
        if opcao == "1":
            cadastrar_usuario()
        if opcao == "2":
            login()
        if opcao == "3":
            print("Processo finalizado")
            break