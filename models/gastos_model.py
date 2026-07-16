class ControleGastos:
    def __init__(self):
        self.registros = []
        self.proximo_id = 1

    def adicionar_registro(self, tipo, valor, categoria, descricao):
        if categoria.strip() == "":
            categoria = "Sem categoria"
        if descricao.strip() == "":
            descricao = "Sem descrição"

        registro = {
            "id": self.proximo_id,
            "tipo": tipo,
            "valor": valor,
            "categoria": categoria,
            "descricao": descricao,
        }

        self.registros.append(registro)
        self.proximo_id += 1
        return registro

    def listar_todos(self):
        return self.registros

    def pesquisar_por_categoria(self, categoria_procurada):
        categoria_procurada = categoria_procurada.strip().lower()
        encontrados = []
        for registro in self.registros:
            if registro["categoria"].lower() == categoria_procurada:
                encontrados.append(registro)
        return encontrados

    def calcular_saldo(self):
        total_receitas = 0.0
        total_despesas = 0.0
        for registro in self.registros:
            if registro["tipo"] == "receita":
                total_receitas += registro["valor"]
            else:
                total_despesas += registro["valor"]
        saldo = total_receitas - total_despesas
        return saldo, total_receitas, total_despesas

    def excluir_registro(self, id_excluir):
        for registro in self.registros:
            if registro["id"] == id_excluir:
                self.registros.remove(registro)
                return True
        return False