class UsuarioModel:
    def __init__(self):
        self.usuarios = {
            "admin": "admin123"
        }

    def validar_login(self, login, senha):
        if login in self.usuarios:
            return self.usuarios[login] == senha
        return False

    def pesquisar_usuario(self, login):
        return login in self.usuarios

    def inserir_usuario(self, login, senha):
        self.usuarios[login] = senha

    def remover_usuario(self, login):
        if login in self.usuarios:
            del self.usuarios[login]
            return True
        return False

    def listar_usuarios(self):
        return list(self.usuarios.keys())


usuario_model = UsuarioModel()