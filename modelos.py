from flask_sqlalchemy import SQLAlchemy

# Instanciar SQLAlchemy
db = SQLAlchemy()

### MODELOS ###

# Creamos el modelo de database
class One_piece(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(30), nullable=False)
    tripulacion = db.Column(db.String(30))
    crimen = db.Column(db.String(100))
    recompensa = db.Column(db.String(15))