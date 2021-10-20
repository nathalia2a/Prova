import flask 
from flask_restful import Resource, Api
import json

app = flask.Flask(_name_)
api = Api(app)

receita = [
{
    'titulo': "Miojo",
    'lista de ingredientes':[
        "Miojo",
        "Manteiga",
        "água",
    ],
    'modo de preparo': " Esquente a água por um minuto, depois adicione o macarrão, após cozihar adicione o tempeiro e a manteiga ...",
    'rendimento': "1 porção "
}
]

class Recs(Resource):
    def get(self):
        return {'status': 200, 'data': receita}

    def post(self):
        newRec = json.loads(flask.request.data)
        receita.append(newRec)
        return {
            "message": "Updated!",
            "new": newRec
        }

class Rec(Resource):
    def get(self, indice):
        try:
            return receita[indice]
        except IndexError:
            messagem = "Indice {} não encontrado!".format(indice)
            return {'status': "Erro de índice!"
                              "mensage"}
        except:
            messagem = "Erro desconhecido"
            return {
                "status": "Erro de índice",
                "mensage": messagem,
            }


    def put(self, indice):
        newValue = json.loads(flask.request.data)
        receita[indice] = newValue
        return {
            "message": "Updated!",
            "new": newValue
        }

    def delete(self, indice):
        receita.pop(indice)
        return {
            "message": "Deleted!",
            "Lista de Receitas": receita
        }

api.add_resource(Recs,'/recs/')
api.add_resource(Rec,'/recs/<int:indice>')

app.run(debug=True)
if _name_ != '_main_':
    pass