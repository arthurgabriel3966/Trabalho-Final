def exibir_menu():
    print("=" * 40)
    print("   SISTEMA DE CONTROLE DE GASTOS")
    print("=" * 40)
    print("1 - Cadastrar receita")
    print("2 - Cadastrar despesa")
    print("3 - Listar todos os registros")
    print("4 - Pesquisar gastos por categoria")
    print("5 - Mostrar saldo atual")
    print("6 - Excluir um registro")
    print("0 - Fazer Logout")
    print("=" * 40)


def exibir_registros(lista):
    print("\n--- Lista de Registros ---")

    if len(lista) == 0:
        print("Nenhum registro encontrado.\n")
        return

    for registro in lista:
        sinal = "+" if registro["tipo"] == "receita" else "-"
        print(
            f"ID: {registro['id']} | {registro['tipo'].capitalize()} | "
            f"{sinal}R$ {registro['valor']:.2f} | "
            f"Categoria: {registro['categoria']} | "
            f"Descrição: {registro['descricao']}"
        )
    print()


def exibir_saldo(saldo, total_receitas, total_despesas):
    print("\n--- Saldo Atual ---")
    print(f"Total de receitas: R$ {total_receitas:.2f}")
    print(f"Total de despesas: R$ {total_despesas:.2f}")

    if saldo >= 0:
        print(f"Saldo disponível: R$ {saldo:.2f}")
    else:
        print(f"Saldo negativo: -R$ {abs(saldo):.2f}")
    print()


def pedir_dados_registro():
    valor_valido = False
    valor = 0.0

    while not valor_valido:
        entrada = input("Valor (R$): ").replace(",", ".")
        try:
            valor = float(entrada)
            if valor <= 0:
                print("O valor deve ser maior que zero. Tente novamente.")
            else:
                valor_valido = True
        except ValueError:
            print("Valor inválido. Digite apenas números. Tente novamente.")

    categoria = input("Categoria (ex: Alimentação, Transporte, Salário): ")
    descricao = input("Descrição: ")

    return valor, categoria, descricao


def pedir_categoria_pesquisa():
    return input("\nDigite a categoria que deseja pesquisar: ")


def pedir_id_exclusao():
    entrada = input("\nDigite o ID do registro que deseja excluir: ")
    try:
        return int(entrada)
    except ValueError:
        return None