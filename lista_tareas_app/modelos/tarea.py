# Clase que representa una tarea del sistema
class Tarea:
    def __init__(self, id_tarea, descripcion):
        # Guarda el identificador de la tarea
        self.id_tarea = id_tarea

        # Guarda la descripción escrita por el usuario
        self.descripcion = descripcion

        # La tarea inicia como no completada
        self.completada = False

    def marcar_completada(self):
        # Cambia el estado de la tarea a completada
        self.completada = True

    def obtener_texto_mostrable(self):
        # Devuelve el texto que verá el usuario en la interfaz
        if self.completada:
            return f"[Hecho] {self.descripcion}"
        return self.descripcion