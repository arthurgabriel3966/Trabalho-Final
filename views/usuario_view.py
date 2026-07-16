def exibir_menu_inicial():
    print("=" * 40)
    print("      TELA DE ACESSO")
    print("=" * 40)
    print("1 - Fazer Login")
    print("2 - Criar Nova Conta")
    print("0 - Sair do Programa")
    print("=" * 40)


def pedir_dados_usuario():
    login = input("Usuário: ").strip()
    senha = input("Senha: ")
    return login, senha