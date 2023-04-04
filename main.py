from flask import Flask, Response
import json
from models.categoria import Categoria
from models.produtos import Produto

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/projetocrud'

@app.route("/categorias", methods=["GET"])
def seleciona_categorias():
    categorias_objetos = Categoria.query.all()
    categorias_json = [categoria.to_json() for categoria in categorias_objetos]
    return gera_response(200, "categoria", categorias_json)


@app.route("/produtos", methods=["GET"])
def seleciona_produtos():
    produtos_objetos = Produto.query.all()
    produtos_json = [produto.to_json() for produto in produtos_objetos]
    return gera_response(200, "produtos", produtos_json)

def gera_response(status, nome_do_conteudo, conteudo, mensagem=False):
    body = {}
    body[nome_do_conteudo] = conteudo
    if (mensagem):
        body["mensagem"] = mensagem
    return Response(json.dumps(body), status=status, mimetype="application/json")

if __name__ == '__main__':
    from sql_alchemy import db
    db.init_app(app)
    app.run(debug=True)