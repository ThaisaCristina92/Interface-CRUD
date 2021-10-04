import mysql.connector

class Banco():

    def __init__(self):
        self.conexao = mysql.connector.connect(host='localhost', user='root', password='thaisa', database='cadastropython')
        self.createTable()
        print("Database connection made!")

    def createTable(self):
        c = self.conexao.cursor()

        #c.execute("""create table if not exists usuarios ( idusuario integer primary key autoincrement , nome text, telefone text, email text, usuario text, senha text)""")
        self.conexao.commit()
        c.close()

class Usuarios(object):


    def __init__(self, idusuario = 0, nome = "", telefone = "", email = "", usuario = "", senha = ""):
        self.info = {}
        self.idusuario = idusuario
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.usuario = usuario
        self.senha = senha


    def insertUser(self):

        banco = Banco()
        try:

            c = banco.conexao.cursor()

            #c.execute(" INSERT INTO table tbl_pessoas  (idusuario, nome, telefone, email , usuario, senha) values ('" + self.nome + "', '" + self.telefone + "', '" + self.email + "', '" +            self.usuario + "', '" + self.senha + "' )")
            c.execute ("insert into tbl_pessoas (Nome, Telefone, Email, Usuario, Senha) Values ('" + self.nome + "', '" + self.telefone + "', '" + self.email + "', '" +            self.usuario + "', '" + self.senha + "')");            
            banco.conexao.commit()
            c.close()

            return "Usuário cadastrado com sucesso!"
        except:
            return "Ocorreu um erro na inserção do usuário"

    def updateUser(self):

        banco = Banco()
        try:

            c = banco.conexao.cursor()

            c.execute("UPDATE tbl_pessoas SET nome = '" + self.nome + "', telefone = '" + self.telefone + "', email = '" + self.email + "', usuario = '" + self.usuario + "', senha = '" + self.senha + "' where idusuario = " + self.idusuario + " ")

            banco.conexao.commit()
            c.close()

            return "Usuário atualizado com sucesso!"
        except:
            return "Ocorreu um erro na alteração do usuário"

    def deleteUser(self):

        banco = Banco()
        try:

            c = banco.conexao.cursor()

            c.execute("delete from tbl_pessoas where idusuario = " + self.idusuario + " ")

            banco.conexao.commit()
            c.close()

            return "Usuário excluído com sucesso!"
        except:
            return "Ocorreu um erro na exclusão do usuário"

    def selectUser(self, idusuario):
        banco = Banco()
        try:

            c = banco.conexao.cursor()

            c.execute("Select * from tbl_pessoas where idusuario = " + idusuario + "  ")

            for linha in c:
                self.idusuario = linha[0]
                self.nome = linha[1]
                self.telefone = linha[2]
                self.email = linha[3]
                self.usuario = linha[4]
                self.senha = linha[5]

            c.close()

            return "Busca feita com sucesso!"
        except:
            return "Ocorreu um erro na busca do usuário"