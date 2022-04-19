from .. import db

class users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    rol = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    def __repr__(self):
        return '<Usuario: %r %r >' % (self.firstname, self.password, self.rol, self.email)
    
    
    #Conversion objeto - JSON
    
    
    def to_json(self):
        usuario_json = {
            'id': self.id,
            'name': str(self.name),
            'password': str(self.password),
            'rol' : str(self.rol),
            'email': str(self.email),

        }
        return usuario_json

    def to_json_short(self):
        usuario_json = {
            'id': self.id,
            'name': str(self.name),
            'password': str(self.password),
            'rol' : str(self.rol),
            'email': str(self.email),

        }
        return usuario_json
    @staticmethod
    #conversion JSON - objeto
    def from_json(usuario_json):
        id = usuario_json.get('id')
        name = usuario_json.get('name')
        password = usuario_json.get('password')
        rol = usuario_json.get('rol')
        email = usuario_json.get('email')
        return Users (id = id,
            name = name,
            password = password,
            rol = rol,
            email =email)