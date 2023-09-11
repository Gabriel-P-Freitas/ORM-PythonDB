from database import db #Importação da variável db, ou seja, o nosso banco de dados, para assim migrar os dados nele

class Empresa(db.Model):
    __tablename__ = "empresa"
    id = db.Column(db.Integer, primary_key= True)
    empregado = db.Column(db.String(100))
    cargo = db.Column(db.String(100))

    def __init__(self, empregado, cargo):
        self.empregado = empregado
        self.cargo = cargo

    # Os dados dessa classe serão usados no banco de dados para o armazenamento nas tabelas, colunas etc.