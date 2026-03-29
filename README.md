# Semana 15 - Aplicación GUI "Lista de Tareas" con Eventos y Ejecutable

## Descripción del proyecto

En esta tarea desarrollé una aplicación de escritorio en Python utilizando Tkinter. La aplicación permite agregar, completar y eliminar tareas mediante una interfaz gráfica sencilla y fácil de usar.

El proyecto fue organizado siguiendo una arquitectura modular por capas, separando el modelo, la lógica del sistema y la interfaz gráfica, tal como se solicita en la guía. Además, se aplicó manejo de eventos con botones, teclado y ratón para mejorar la interacción del usuario con la aplicación.

## Objetivo

Desarrollar una aplicación GUI tipo lista de tareas que permita gestionar actividades diarias, aplicando correctamente los conceptos fundamentales de manejo de eventos en Tkinter y respetando la estructura modular del proyecto.

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
Explicación de los archivos
main.py: punto de inicio de la aplicación.
modelos/tarea.py: define la clase Tarea con sus atributos y estado.
servicios/tarea_servicio.py: contiene la lógica para agregar, completar, eliminar y listar tareas.
ui/app_tkinter.py: construye la interfaz gráfica y maneja los eventos del usuario.
Funcionalidades principales
Agregar nuevas tareas
Marcar tareas como completadas
Eliminar tareas
Añadir tareas con el botón Añadir Tarea
Añadir tareas con la tecla Enter
Marcar tareas como completadas con doble clic
Mostrar un cambio visual cuando una tarea ha sido completada
Manejo de eventos aplicado

En esta aplicación se utilizaron dos formas principales de manejo de eventos:

Eventos con command

Se aplicaron en los botones para ejecutar acciones directas como:

añadir tarea
marcar completada
eliminar tarea
Eventos con .bind()

Se implementaron para responder a acciones del usuario de forma más dinámica:

<Return> para agregar una tarea presionando la tecla Enter
<Double-1> para marcar una tarea como completada con doble clic sobre la lista
Feedback visual

Cuando una tarea se marca como completada:

su estado cambia a Completada
en la descripción aparece [Hecho]
se muestra un cambio visual en la interfaz para diferenciarla de las tareas pendientes
Tecnologías utilizadas
Python
Tkinter
Git
GitHub
PyInstaller
Cómo ejecutar el proyecto

Primero se debe ingresar a la carpeta del proyecto:

cd lista_tareas_app

Luego ejecutar:

python main.py
Generación del ejecutable

Para compilar la aplicación como ejecutable se utilizó PyInstaller con el siguiente comando:

pyinstaller --noconsole --onefile --name ListaTareasApp main.py

El archivo ejecutable generado se encuentra en la carpeta:

lista_tareas_app/dist/ListaTareasApp.exe
Conclusión

Con esta tarea pude aplicar de forma práctica los conceptos de manejo de eventos en interfaces gráficas. También reforcé la importancia de organizar correctamente un proyecto por capas, separando la lógica del sistema de la interfaz visual. El resultado fue una aplicación funcional, clara y acorde a lo solicitado en la guía.

Autor

Jorge Sánchez
