from models.gastos_model import ControleGastos
import views.gastos_view as g_view
import views.comum_view as c_view


def executar_controle_gastos():
    model = ControleGastos()
    opcao = -1

    while opcao != 0:
        g_view.exibir_menu()
        entrada = c_view.pedir_opcao_menu()

        if not entrada.isdigit():
            c_view.exibir_mensagem("\nOpção inválida. Digite um número do menu.\n")
            continue

        opcao = int(entrada)

        if opcao == 1:
            c_view.exibir_mensagem("\n--- Cadastrar receita ---")
            valor, categoria, descricao = g_view.pedir_dados_registro()
            model.adicionar_registro("receita", valor, categoria, descricao)
            c_view.exibir_mensagem("Receita cadastrada com sucesso!\n")

        elif opcao == 2:
            c_view.exibir_mensagem("\n--- Cadastrar despesa ---")
            valor, categoria, descricao = g_view.pedir_dados_registro()
            model.adicionar_registro("despesa", valor, categoria, descricao)
            c_view.exibir_mensagem("Despesa cadastrada com sucesso!\n")

        elif opcao == 3:
            g_view.exibir_registros(model.listar_todos())

        elif opcao == 4:
            categoria = g_view.pedir_categoria_pesquisa()
            encontrados = model.pesquisar_por_categoria(categoria)
            if len(encontrados) == 0:
                c_view.exibir_mensagem("Nenhum registro encontrado para essa categoria.\n")
            else:
                g_view.exibir_registros(encontrados)

        elif opcao == 5:
            saldo, total_receitas, total_despesas = model.calcular_saldo()
            g_view.exibir_saldo(saldo, total_receitas, total_despesas)

        elif opcao == 6:
            if len(model.listar_todos()) == 0:
                c_view.exibir_mensagem("\nNão há registros para excluir.\n")
                continue
            g_view.exibir_registros(model.listar_todos())
            id_excluir = g_view.pedir_id_exclusao()
            if id_excluir is None:
                c_view.exibir_mensagem("ID inválido.\n")
            elif model.excluir_registro(id_excluir):
                c_view.exibir_mensagem("Registro excluído com sucesso!\n")
            else:
                c_view.exibir_mensagem("Registro não encontrado.\n")

        elif opcao == 0:
            c_view.exibir_mensagem("\nFazendo logout...")