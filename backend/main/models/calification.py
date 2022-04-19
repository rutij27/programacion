
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