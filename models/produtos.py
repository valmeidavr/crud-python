from sql_alchemy import db

class Produto(db.Model):
    __tablename__ = 'produtos'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50))
    quantidade = db.Column(db.Integer)
    preco = db.Column(db.Float(precision=2))
    status = db.Column(db.Boolean, default=True, nullable=False)
    categoria_id = db.Column(db.Integer, db.ForeignKey('categorias.id'), nullable=False)

    def to_json(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "status": self.status,
            "categoria_id": self.categoria_id
        }