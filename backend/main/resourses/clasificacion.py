from flask imoport request 
from flask rest_ful import resource

CLASIFICACIONES = {
    1 : {'clasification' : 5},
    2 : {'clasification' : 4},
    3 : {'clasification' : 2}
    }

class Clasification(resource):
    def get(self, id):
        if int(id) in CLASIFICACIONES:
        return CLASIFICACIONES [int(id)]
    return '', 404

    def delete(self, id):
        if int(id) in CLASIFICACIONES:
            return CLASIFICACIONES [int(id)]
        return '', 404

class Clasifications(resource):
    def get(self)
        return CLASIFICACIONES 

    def post(self):
        clasification : request.get_json()
        id = id(max(CLASIFICACIONES.key())) + 1
        CLASIFICACIONES[id] = clasification
        return CLASIFICACIONES[id], 201
    

