import tkinter as tk
import math

class CalculadoraCientifica:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora Científica")
        self.root.resizable(0, 0)

        # Variable para almacenar la expresión mostrada
        self.expression = ""
        self.input_text = tk.StringVar()

        # Marco para la pantalla
        frame_pantalla = tk.Frame(root, height=50, bd=5, relief=tk.RIDGE)
        frame_pantalla.pack(expand=True, fill="both")

        # Campo de entrada
        self.entry = tk.Entry(frame_pantalla, font=("Arial", 18), textvariable=self.input_text,
                              justify="right", bd=10, insertwidth=4)
        self.entry.pack(expand=True, fill="both")

        # Marco para los botones
        frame_botones = tk.Frame(root, bd=5, relief=tk.RIDGE)
        frame_botones.pack()

        # Definir los botones en una matriz (fila, columna, texto, ancho (opcional))
        botones = [
            # Fila 1
            ["sin", "cos", "tan", "asin", "acos", "atan"],
            # Fila 2
            ["log", "ln", "√", "^", "!", "C"],
            # Fila 3
            ["7", "8", "9", "/", "(", ")"],
            # Fila 4
            ["4", "5", "6", "*", "π", "e"],
            # Fila 5
            ["1", "2", "3", "-", "←", "AC"],
            # Fila 6
            ["0", ".", "=", "+", "", ""]  # celdas vacías para ajustar
        ]

        # Crear botones dinámicamente
        for i, fila in enumerate(botones):
            for j, texto in enumerate(fila):
                if texto == "":
                    continue
                # Determinar el ancho y color según el tipo de botón
                if texto in ["sin", "cos", "tan", "asin", "acos", "atan", "log", "ln", "√", "^", "!", "π", "e"]:
                    color = "lightblue"
                    ancho = 6
                elif texto in ["C", "AC", "←"]:
                    color = "orange"
                    ancho = 6
                elif texto in ["="]:
                    color = "lightgreen"
                    ancho = 12  # Ocupa más espacio
                else:
                    color = "lightgray"
                    ancho = 6

                # Crear el botón
                btn = tk.Button(frame_botones, text=texto, width=ancho, height=2, bg=color,
                                font=("Arial", 12), command=lambda x=texto: self.boton_click(x))
                btn.grid(row=i, column=j, padx=1, pady=1, sticky="nsew")

        # Ajustar el botón "=" para que ocupe dos columnas
        # Pero como lo definimos en la matriz, necesita un tratamiento especial
        # Buscamos el botón "=" y le cambiamos el colspan
        # Es más fácil: después de crear todos, modificamos el botón de "="
        # Lo identificamos por su texto y le asignamos columnspan=2
        for widget in frame_botones.children.values():
            if widget["text"] == "=":
                widget.grid_configure(columnspan=1)

        # Ajustar pesos de las columnas para que se expandan
        for i in range(6):
            frame_botones.columnconfigure(i, weight=1)

    def boton_click(self, valor):
        """Maneja el evento de click en cada botón"""
        if valor == "C":  # Borrar último carácter
            self.expression = self.expression[:-1]
        elif valor == "AC":  # Borrar todo
            self.expression = ""
        elif valor == "←":  # Retroceso (igual que C)
            self.expression = self.expression[:-1]
        elif valor == "=":
            self.calcular()
            return
        elif valor == "π":
            self.expression += str(math.pi)
        elif valor == "e":
            self.expression += str(math.e)
        elif valor == "√":
            self.expression += "math.sqrt("
        elif valor == "^":
            self.expression += "**"
        elif valor == "!":
            self.expression += "math.factorial("
        elif valor == "log":
            self.expression += "math.log10("
        elif valor == "ln":
            self.expression += "math.log("
        elif valor in ["sin", "cos", "tan", "asin", "acos", "atan"]:
            self.expression += f"math.{valor}("
        else:
            self.expression += str(valor)

        # Actualizar la pantalla
        self.input_text.set(self.expression)

    def calcular(self):
        """Evalúa la expresión de forma segura y muestra el resultado"""
        try:
            # Restringir el entorno de evaluación solo a funciones matemáticas y constantes
            # math.__dict__ contiene todas las funciones y constantes (pi, e, etc.)
            # También incluimos '__builtins__': None para evitar código malicioso
            resultado = eval(self.expression, {"__builtins__": None}, math.__dict__)
            self.expression = str(resultado)
        except:
            self.expression = "Error"
        finally:
            self.input_text.set(self.expression)

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculadoraCientifica(root)
    root.mainloop()