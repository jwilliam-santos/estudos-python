import tkinter as tk
from tkinter import ttk


class Aplicação(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Conversor")
        self.cria_quadro()

    def cria_quadro(self):
        self.quadro = ttk.Frame(self)
        self.l_temperatura = ttk.Label(self.quadro, text="Temperatura:")
        self.l_temperatura.pack()
        self.temperatura = ttk.Entry(self.quadro)
        self.temperatura.pack()
        self.botao_CF = ttk.Button(
            self.quadro,
            text="Celsius para Fahrenheit",
            command=self.celsius_para_fahrenheit,
        )
        self.botao_CF.pack()
        self.botao_FC = ttk.Button(
            self.quadro,
            text="Fahrenheit para Celsius",
            command=self.fahrenheit_para_celsius,
        )
        self.botao_FC.pack()
        self.l_resultado = ttk.Label(self.quadro, text="Resultado")
        self.l_resultado.pack()
        self.quadro.pack(expand=True)

    def celsius_para_fahrenheit(self):
        temperatura = float(self.temperatura.get())
        fahrenheit = 9 / 5.0 * temperatura + 32
        self.l_resultado["text"] = f"{fahrenheit:5.2f} \u00b0F"

    def fahrenheit_para_celsius(self):
        temperatura = float(self.temperatura.get())
        celsius = (temperatura - 32) * 5 / 9.0
        self.l_resultado["text"] = f"{celsius:5.2f} \u00b0C"


raiz = Aplicação()
raiz.mainloop()