from database import db #Importação da variável db, ou seja, o nosso banco de dados, para assim migrar os dados nele

class Diario(db.Model):
    __tablename__= "diario"
    id = db.Column(db.Integer, primary_key = True)
    titulo = db.Column(db.String(100))
    disciplina = db.Column(db.String(100))

    def __init__(self, titulo, disciplina):
        self.titulo = titulo
        self.disciplina = disciplina

        # Os dados dessa classe serão usados no banco de dados para o armazenamento nas tabelas, colunas etc.