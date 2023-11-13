from flask import Flask, render_template, request, redirect, url_for
from modelos import db, One_piece

# Instanciar la clase flask 
app = Flask(__name__)

# Configuramos la base de datos
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///database.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializar nuestra db 
db.init_app(app)

### RUTAS ###

# Ruta read - leer 
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/piratas')
def piratas():

    # Obtener los personajes de One Piece 
    personajes = One_piece.query.all()

    return render_template('piratas.html', personajes=personajes)

# Ruta create - crear
@app.route('/report', methods=['GET', 'POST'])
def report():

    # Obtener los personajes de One Piece 
    personajes = One_piece.query.all()

    if request.method  == 'POST':

        # Obtener los datos de mi formulario
        nombre = request.form.get('nombre')
        tripulacion = request.form.get('tripulacion')
        recompensa = request.form.get('recompensa')
        crimen = request.form.get('crimen')
        # Creamos el objeto personaje
        personaje = One_piece(nombre=nombre, tripulacion=tripulacion, recompensa=recompensa, crimen=crimen)

        # Agregar a la db
        db.session.add(personaje)

        # Guardamos los cambios
        db.session.commit()

        return redirect('piratas')
    return render_template('report.html')

@app.route('/eliminar/<id>')
def eliminar(id):

    # Obtener el personaje a eliminar
    personajes = One_piece.query.get(id)

    # Eliminamos el personaje seleccionado
    db.session.delete(personajes)

    # Guardamos los cambios
    db.session.commit()

    return redirect(url_for('piratas'))



@app.route('/editar/<id>', methods=['GET', 'POST'])
def editar(id):
    # Obtener el personaje a editar
    personaje = One_piece.query.get(id)

    if request.method == 'POST':
        # Obtener los datos de mi formulario
        personaje.nombre = request.form.get('nombre')
        personaje.tripulacion = request.form.get('tripulacion')
        personaje.recompensa = request.form.get('recompensa')
        personaje.crimen = request.form.get('crimen')

        # Guardar los cambios en la base de datos
        db.session.commit()
        
        return redirect(url_for('piratas'))
    return render_template('editar.html', personaje=personaje)



### BREAKPOINT ###
if __name__ == '__main__':
    app.run(debug=True)