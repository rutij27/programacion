
from .. import db

class calification(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    puntos = db.Column(db.String(100), nullable=False)
    comento = db.Column(db.String(100), nullable=False)
    user_id = db.Column(db.String(100), nullable=False)
    poema_id = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return '<User: %r %r >' % (self.id, self.puntaje, self.comentario, self.userID, self.poemaID)

    def to_json(self):
        calificacion_json = {
            'id': self.id,
            'puntos': str(self.puntos),
            'comento': str(self.comento),
            'user_id': str(self.user_id),
            'poema_id': str(self.poema_),

        }
        return calificacion_json

    def to_json_short(self):
        calificacion_json = {
            'id': self.id,
            'puntos': str(self.puntos),
            'comento': str(self.comento),
            'user_id': str(self.user_id),
            'poema_id': str(self.poema_id),
        }
        return calificacion_json
    
    @staticmethod

    def from_json(user_json):
        id = user_json.get('id')
        puntos = user_json.get('puntos')
        comento = user_json.get('comento')
        user_id = user_json.get('user_id')
        poema_id = user_json.get('poema_id')

        return Calification(id=id,
                    puntos=puntos,
                    comento=comento,
                    user_id=user_id,
                    poema_id=poema_id
                    )

