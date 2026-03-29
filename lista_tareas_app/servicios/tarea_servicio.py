from modelos.tarea import Tarea


# Clase que maneja toda la lógica del sistema
class TareaServicio:
    def __init__(self):
        # Lista donde se guardan las tareas
        self.tareas = []

        # Contador para generar ids únicos
        self.siguiente_id = 1

    def agregar_tarea(self, descripcion):
        # Evita guardar tareas vacías
        descripcion = descripcion.strip()
        if not descripcion:
            return None

        # Crea la nueva tarea
        nueva_tarea = Tarea(self.siguiente_id, descripcion)

        # La agrega a la lista
        self.tareas.append(nueva_tarea)

        # Aumenta el id para la próxima tarea
        self.siguiente_id += 1

        return nueva_tarea

    def obtener_tareas(self):
        # Devuelve la lista completa de tareas
        return self.tareas

    def completar_tarea(self, id_tarea):
        # Busca la tarea por su id y la marca como completada
        for tarea in self.tareas:
            if tarea.id_tarea == id_tarea:
                tarea.marcar_completada()
                return True
        return False

    def eliminar_tarea(self, id_tarea):
        # Busca la tarea por su id y la elimina
        for tarea in self.tareas:
            if tarea.id_tarea == id_tarea:
                self.tareas.remove(tarea)
                return True
        return False