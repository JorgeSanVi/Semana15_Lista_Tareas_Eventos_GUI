import tkinter as tk

from ui.app_tkinter import AppTkinter


# Punto de inicio de la aplicación
def main():
    root = tk.Tk()
    AppTkinter(root)
    root.mainloop()


if __name__ == "__main__":
    main()