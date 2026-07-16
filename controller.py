from model import ControleGastos, usuario_model
import view


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


def executar_controle_gastos():
    model = ControleGastos()
    opcao = -1

    while opcao != 0:
        view.exibir_menu()
        entrada = view.pedir_opcao_menu()

        if not entrada.isdigit():
            view.exibir_mensagem("\nOpção inválida. Digite um número do menu.\n")
            continue

        opcao = int(entrada)

        if opcao == 1:
            view.exibir_mensagem("\n--- Cadastrar receita ---")
            valor, categoria, descricao = view.pedir_dados_registro()
            model.adicionar_registro("receita", valor, categoria, descricao)
            view.exibir_mensagem("Receita cadastrada com sucesso!\n")

        elif opcao == 2:
            view.exibir_mensagem("\n--- Cadastrar despesa ---")
            valor, categoria, descricao = view.pedir_dados_registro()
            model.adicionar_registro("despesa", valor, categoria, descricao)
            view.exibir_mensagem("Despesa cadastrada com sucesso!\n")

        elif opcao == 3:
            view.exibir_registros(model.listar_todos())

        elif opcao == 4:
            categoria = view.pedir_categoria_pesquisa()
            encontrados = model.pesquisar_por_categoria(categoria)
            if len(encontrados) == 0:
                view.exibir_mensagem("Nenhum registro encontrado para essa categoria.\n")
            else:
                view.exibir_registros(encontrados)

        elif opcao == 5:
            saldo, total_receitas, total_despesas = model.calcular_saldo()
            view.exibir_saldo(saldo, total_receitas, total_despesas)

        elif opcao == 6:
            if len(model.listar_todos()) == 0:
                view.exibir_mensagem("\nNão há registros para excluir.\n")
                continue
            view.exibir_registros(model.listar_todos())
            id_excluir = view.pedir_id_exclusao()
            if id_excluir is None:
                view.exibir_mensagem("ID inválido.\n")
            elif model.excluir_registro(id_excluir):
                view.exibir_mensagem("Registro excluído com sucesso!\n")
            else:
                view.exibir_mensagem("Registro não encontrado.\n")

        elif opcao == 0:
            view.exibir_mensagem("\nFazendo logout...")


def executar():
    opcao = -1
    while opcao != 0:
        view.exibir_menu_inicial()
        entrada = view.pedir_opcao_menu()

        if not entrada.isdigit():
            view.exibir_mensagem("\nOpção inválida.\n")
            continue

        opcao = int(entrada)

        if opcao == 1:
            view.exibir_mensagem("\n--- LOGIN ---")
            login, senha = view.pedir_dados_usuario()
            if controlador_login(login, senha):
                view.exibir_mensagem(f"\nBem-vindo, {login}! Acesso liberado.\n")
                executar_controle_gastos()
            else:
                view.exibir_mensagem("\nErro: Usuário ou senha incorretos!\n")

        elif opcao == 2:
            view.exibir_mensagem("\n--- CRIAR CONTA ---")
            login, senha = view.pedir_dados_usuario()
            sucesso, msg = controlador_inserir_usuario(login, senha)
            view.exibir_mensagem(f"\n{msg}\n")

        elif opcao == 0:
            view.exibir_mensagem("\nFechando programa. Até logo!")
