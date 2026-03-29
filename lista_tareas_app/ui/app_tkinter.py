import tkinter as tk
from tkinter import ttk, messagebox

from servicios.tarea_servicio import TareaServicio


# Clase encargada de la interfaz gráfica y los eventos
class AppTkinter:
    def __init__(self, root):
        # Ventana principal
        self.root = root
        self.root.title("Lista de Tareas")
        self.root.geometry("700x450")
        self.root.resizable(False, False)

        # Servicio que maneja la lógica del sistema
        self.servicio = TareaServicio()

        # Crea los componentes visuales
        self.crear_componentes()

        # Configura los eventos adicionales con bind()
        self.configurar_eventos()

    def crear_componentes(self):
        # Título principal
        titulo = tk.Label(
            self.root,
            text="Lista de Tareas",
            font=("Arial", 16, "bold")
        )
        titulo.pack(pady=10)

        # Marco superior para entrada y botón de añadir
        marco_superior = tk.Frame(self.root)
        marco_superior.pack(pady=10)

        # Campo donde el usuario escribe la tarea
        self.entry_tarea = tk.Entry(marco_superior, width=40, font=("Arial", 12))
        self.entry_tarea.grid(row=0, column=0, padx=5)

        # Botón para agregar tarea
        self.boton_agregar = tk.Button(
            marco_superior,
            text="Añadir Tarea",
            width=15,
            command=self.agregar_tarea
        )
        self.boton_agregar.grid(row=0, column=1, padx=5)

        # Marco para botones de acción
        marco_botones = tk.Frame(self.root)
        marco_botones.pack(pady=10)

        # Botón para marcar completada
        self.boton_completar = tk.Button(
            marco_botones,
            text="Marcar Completada",
            width=18,
            command=self.marcar_completada
        )
        self.boton_completar.grid(row=0, column=0, padx=5)

        # Botón para eliminar tarea
        self.boton_eliminar = tk.Button(
            marco_botones,
            text="Eliminar",
            width=15,
            command=self.eliminar_tarea
        )
        self.boton_eliminar.grid(row=0, column=1, padx=5)

        # Marco de la lista
        marco_lista = tk.Frame(self.root)
        marco_lista.pack(pady=10, fill="both", expand=True)

        # Treeview para mostrar las tareas
        self.tree = ttk.Treeview(
            marco_lista,
            columns=("ID", "Descripción", "Estado"),
            show="headings",
            height=12
        )
        self.tree.heading("ID", text="ID")
        self.tree.heading("Descripción", text="Descripción")
        self.tree.heading("Estado", text="Estado")

        self.tree.column("ID", width=60, anchor="center")
        self.tree.column("Descripción", width=430, anchor="w")
        self.tree.column("Estado", width=150, anchor="center")

        self.tree.pack(side="left", fill="both", expand=True)

        # Barra de desplazamiento
        scrollbar = ttk.Scrollbar(marco_lista, orient="vertical", command=self.tree.yview)
        scrollbar.pack(side="right", fill="y")
        self.tree.configure(yscrollcommand=scrollbar.set)

        # Estilo visual para tareas completadas
        self.tree.tag_configure("completada", foreground="gray")

    def configurar_eventos(self):
        # Agrega tarea al presionar Enter en el campo de texto
        self.entry_tarea.bind("<Return>", self.agregar_tarea_evento)

        # Marca como completada al hacer doble clic en una tarea
        self.tree.bind("<Double-1>", self.marcar_completada_evento)

    def agregar_tarea(self):
        # Obtiene el texto escrito por el usuario
        descripcion = self.entry_tarea.get()

        # Intenta agregar la tarea usando la capa de servicio
        tarea = self.servicio.agregar_tarea(descripcion)

        # Si está vacía, muestra aviso
        if tarea is None:
            messagebox.showwarning("Aviso", "Debe escribir una tarea.")
            return

        # Limpia el campo y actualiza la lista
        self.entry_tarea.delete(0, tk.END)
        self.entry_tarea.focus()
        self.actualizar_lista()

    def agregar_tarea_evento(self, event):
        # Llama al mismo método de agregar, pero desde Enter
        self.agregar_tarea()

    def marcar_completada(self):
        # Obtiene el id de la tarea seleccionada
        id_tarea = self.obtener_id_seleccionada()

        if id_tarea is None:
            messagebox.showwarning("Aviso", "Seleccione una tarea.")
            return

        # Marca la tarea como completada
        self.servicio.completar_tarea(id_tarea)
        self.actualizar_lista()

    def marcar_completada_evento(self, event):
        # Permite completar una tarea con doble clic
        self.marcar_completada()

    def eliminar_tarea(self):
        # Obtiene el id de la tarea seleccionada
        id_tarea = self.obtener_id_seleccionada()

        if id_tarea is None:
            messagebox.showwarning("Aviso", "Seleccione una tarea para eliminar.")
            return

        # Elimina la tarea seleccionada
        self.servicio.eliminar_tarea(id_tarea)
        self.actualizar_lista()

    def obtener_id_seleccionada(self):
        # Obtiene el elemento seleccionado en el Treeview
        seleccion = self.tree.selection()

        if not seleccion:
            return None

        # Extrae el id de la primera columna
        valores = self.tree.item(seleccion[0], "values")
        return int(valores[0])

    def actualizar_lista(self):
        # Limpia la lista antes de volver a cargarla
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Inserta nuevamente todas las tareas
        for tarea in self.servicio.obtener_tareas():
            estado = "Completada" if tarea.completada else "Pendiente"

            # Si está completada, se aplica estilo visual diferente
            if tarea.completada:
                self.tree.insert(
                    "",
                    "end",
                    values=(tarea.id_tarea, tarea.obtener_texto_mostrable(), estado),
                    tags=("completada",)
                )
            else:
                self.tree.insert(
                    "",
                    "end",
                    values=(tarea.id_tarea, tarea.obtener_texto_mostrable(), estado)
                )