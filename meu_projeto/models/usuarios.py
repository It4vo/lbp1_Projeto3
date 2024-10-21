class Usuarios:
    def __init__(self,login,senha, tipo=0):
        self.tipo=tipo #1= user 2=admin
        self.login=login
        self.senha=senha
listUsers= []
listUsers.append(Usuarios(rafael, 1234))
Log=Usuarios(rafael, 1234)