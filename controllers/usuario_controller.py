from models.usuario_model import usuario_model
import views.usuario_view as u_view
import views.comum_view as c_view
from controllers.gastos_controller import executar_controle_gastos


def controlador_login(login, senha):
    return usuario_model.validar_login(login, senha)


def controlador_inserir_usuario(login, senha):
    login = login.strip()
    senha = senha.strip()

    if login == "" or senha == "":
        return False, "Login e senha não podem ficar em branco."

    if usuario_model.pesquisar_usuario(login):
        return False, f"O login '{login}' já está cadastrado."

    usuario_model.inserir_usuario(login, senha)
    return True, f"Usuário '{login}' cadastrado com sucesso!"


def executar():
    opcao = -1
    while opcao != 0:
        u_view.exibir_menu_inicial()
        entrada = c_view.pedir_opcao_menu()

        if not entrada.isdigit():
            c_view.exibir_mensagem("\nOpção inválida.\n")
            continue

        opcao = int(entrada)

        if opcao == 1:
            c_view.exibir_mensagem("\n--- LOGIN ---")
            login, senha = u_view.pedir_dados_usuario()
            if controlador_login(login, senha):
                c_view.exibir_mensagem(f"\nBem-vindo, {login}! Acesso liberado.\n")
                executar_controle_gastos()
            else:
                c_view.exibir_mensagem("\nErro: Usuário ou senha incorretos!\n")

        elif opcao == 2:
            c_view.exibir_mensagem("\n--- CRIAR CONTA ---")
            login, senha = u_view.pedir_dados_usuario()
            sucesso, msg = controlador_inserir_usuario(login, senha)
            c_view.exibir_mensagem(f"\n{msg}\n")

        elif opcao == 0:
            c_view.exibir_mensagem("\nFechando programa. Até logo!")