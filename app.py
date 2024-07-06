
from flask import Flask, render_template, request, redirect, url_for, jsonify
from models import db, Tarea

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tareas.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/')
def inicio():
    tareas = Tarea.query.all()
    return render_template('index.html', tareas=tareas)

@app.route('/agregar', methods=['GET', 'POST'])
def agregar_tarea():
    if request.method == 'POST':
        titulo = request.form['titulo']
        descripcion = request.form['descripcion']
        nueva_tarea = Tarea(titulo=titulo, descripcion=descripcion)
        db.session.add(nueva_tarea)
        db.session.commit()
        return redirect(url_for('inicio'))
    return render_template('agregar.html')

@app.route('/editar/<int:tarea_id>', methods=['GET', 'POST'])
def editar_tarea(tarea_id):
    tarea = Tarea.query.get(tarea_id)
    if request.method == 'POST':
        tarea.titulo = request.form['titulo']
        tarea.descripcion = request.form['descripcion']
        db.session.commit()
        return redirect(url_for('inicio'))
    return render_template('editar.html', tarea=tarea)

@app.route('/eliminar/<int:tarea_id>')
def eliminar_tarea(tarea_id):
    tarea = Tarea.query.get(tarea_id)
    if tarea:
        db.session.delete(tarea)
        db.session.commit()
    return redirect(url_for('inicio'))

@app.route('/actualizar/<int:tarea_id>', methods=['POST'])
def actualizar_tarea(tarea_id):
    tarea = Tarea.query.get(tarea_id)
    if tarea:
        data = request.get_json()
        tarea.completado = data['completado']
        db.session.commit()
        return jsonify({'success': True})
    return jsonify({'success': False}), 404

@app.route('/eliminar_completadas', methods=['POST'])
def eliminar_completadas():
    Tarea.query.filter_by(completado=True).delete()
    db.session.commit()
    return jsonify({'success': True})

if __name__ == '__main__':
    app.run(debug=True)
