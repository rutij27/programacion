from flask_restful import Resource
from flask import request


POEMS = {
    1 : {'Nombre del título' : 'P1' ,'Autor' : 'A1'},
    2 : {'Nombre del título' : 'P2' ,'Autor' : 'A2'},
    3 : {'Nombre del título' : 'P3' ,'Autor' : 'A3'},    
}

class Poem(Resource):
    def get(self, id):
        if int(id) in POEMS:
            return POEMS[int(id)]
        return '', 404



    def delete(self, id):
        if int(id) in POEMS:
            return POEMS[int(id)]
        return '', 404

class Poems(Resource):
    def get(self):
        return POEMS
        

    def post(self):
        poem = request.get_json()
        id = int(max(POEMS.key())) + 1
        POEMS[id] = poem
        return POEMS[id], 201