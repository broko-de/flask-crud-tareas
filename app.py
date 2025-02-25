from flask import Flask, request, jsonify
from model import TareaManager

app = Flask(__name__)

tarea_manager = TareaManager()

@app.route('/', methods=['GET'])
def inicio():
    return jsonify({"mensaje": "Bienvenido a la API de tareas de Flask"})

@app.route('/tareas/<int:id>', methods=['GET'])
def obtener_tarea(id):
    tarea = tarea_manager.obtener_tarea(id)
    if tarea:
        return jsonify(tarea)
    return jsonify({"mensaje": "Tarea no encontrada"}), 404

@app.route('/tareas', methods=['GET'])
def listar_tareas():
    return jsonify(tarea_manager.listar_tareas())

@app.route('/tareas', methods=['POST'])
def crear_tarea():
    data = request.json
    nueva_tarea = tarea_manager.crear_tarea(data['nombre'], data['estado'])
    return jsonify(nueva_tarea), 201

@app.route('/tareas/<int:id>', methods=['PUT'])
def editar_tarea(id):
    data = request.json
    tarea = tarea_manager.editar_tarea(id, data['nombre'], data['estado'])
    if tarea:
        return jsonify(tarea)
    return jsonify({"mensaje": "Tarea no encontrada"}), 404

@app.route('/tareas/<int:id>', methods=['DELETE'])
def eliminar_tarea(id):
    if tarea_manager.eliminar_tarea(id):
        return jsonify({"mensaje": "Tarea eliminada"})
    return jsonify({"mensaje": "Tarea no encontrada"}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)