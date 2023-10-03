from database import db

class Professor(db.Model):
    __tablename__ = "professor"
    id = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String(100))

    diario = db.relationship("Diario")

    def __init__(self, nome):
        self.nome = nome