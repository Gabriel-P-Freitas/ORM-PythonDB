from database import db #Importação da variável db, ou seja, o nosso banco de dados, para assim migrar os dados nele

class Diario(db.Model):
    __tablename__= "diario"
    id = db.Column(db.Integer, primary_key = True)
    titulo = db.Column(db.String(100))
    disciplina = db.Column(db.String(100))
    id_professor = db.Column(db.Integer, db.ForeignKey('professor.id'))

    professor = db.relationship('Professor', foreign_keys = id_professor) # Cria a relação com a classe Professor de acordo com seu ID

    def __init__(self, titulo, disciplina, id_professor):
        self.titulo = titulo
        self.disciplina = disciplina
        self.id_professor = id_professor # Referencia a coluna estrangeira

        # Os dados dessa classe serão usados no banco de dados para o armazenamento nas tabelas, colunas etc.