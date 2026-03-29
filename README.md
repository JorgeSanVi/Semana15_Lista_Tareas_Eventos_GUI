# Semana 15 - Lista de Tareas con Eventos

## Descripción del proyecto

En esta tarea desarrollé una aplicación de escritorio en Python utilizando Tkinter. La aplicación permite agregar, completar y eliminar tareas mediante una interfaz gráfica sencilla. Para cumplir con la guía, organicé el proyecto por capas, separando el modelo, la lógica del sistema y la interfaz.

Además, implementé manejo de eventos con botones, teclado y ratón. Se puede agregar una tarea con el botón correspondiente o con la tecla **Enter**, y también marcarla como completada con **doble clic** sobre la lista. Cuando una tarea se completa, su estado cambia visualmente en la interfaz.

## Estructura del proyecto

```plaintext
lista_tareas_app/
│
├── main.py
├── modelos/
│   └── tarea.py
├── servicios/
│   └── tarea_servicio.py
└── ui/
    └── app_tkinter.py

    Funcionalidades principales
Agregar tareas
Marcar tareas como completadas
Eliminar tareas
Añadir tareas con Enter
Completar tareas con doble clic
Mostrar cambio visual en tareas completadas

Tecnologías utilizadas
Python
Tkinter
Git y GitHub
PyInstaller

Ejecución

Desde la carpeta lista_tareas_app, ejecutar:
python main.py