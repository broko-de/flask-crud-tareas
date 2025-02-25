class TareaManager:
    def __init__(self):
        self.tareas = []
        self.id_counter = 1

    def obtener_tarea(self, id):
        return next((tarea for tarea in self.tareas if tarea['id'] == id), None)

    def listar_tareas(self):
        return self.tareas

    def crear_tarea(self, nombre, estado):
        nueva_tarea = {
            'id': self.id_counter,
            'nombre': nombre,
            'estado': estado
        }
        self.tareas.append(nueva_tarea)
        self.id_counter += 1
        return nueva_tarea

    def editar_tarea(self, id, nombre, estado):
        tarea = self.obtener_tarea(id)
        if tarea:
            tarea['nombre'] = nombre
            tarea['estado'] = estado
            return tarea
        return None

    def eliminar_tarea(self, id):
        tarea = self.obtener_tarea(id)
        if tarea:
            self.tareas = [tarea for tarea in self.tareas if tarea['id'] != id]
            return True
        return False