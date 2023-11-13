from flask import Flask
from modelos import db, One_piece

# Instancia de la clase Flask
app = Flask('app')

# Configuramos la base de datos
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///database.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializar la base de datos
db.init_app(app)

# # Crear la base de datos
# with app.app_context():
#   db.create_all()

# Agregamos datos manualmente
with app.app_context():
    # Cargamos los datos de One Piece
    personaje_1 = One_piece(nombre='Monkey D. Luffy', tripulacion='Sombrero de Paja', crimen='Comer los dulces de Big Mom', recompensa='3.000.000.00')
    personaje_2 = One_piece(nombre='Roronoa Zoro', tripulacion='Sombrero de Paja', crimen='Desafiar al Gobierno Mundial', recompensa='1.000.000.000')
    # Agregar a la base de datos
    db.session.add(personaje_1)
    db.session.add(personaje_2)
    db.session.commit()