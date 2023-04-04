from sql_alchemy import db

class Categoria(db.Model):
    __tablename__ = 'categorias'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50))
    status = db.Column(db.Boolean, default=True, nullable=False)
    produtos = db.relationship('Produto', backref='categoria', lazy=True)

    def to_json(self):
       return {
            "id": self.id,
            "nome": self.nome,
            "produtos": [
                {
                    "id": p.id,
                    "nome": p.nome,
                    "valor": p.preco
                } for p in self.produtos] if self.produtos else None,
            "status": self.status
        }

