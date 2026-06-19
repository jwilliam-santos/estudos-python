#Modifique o programa 13.7 para gravar e carregar o desenho em formato JSON.
#Você pode percorrer os objetos do canvas e guardar a form, as coordenadas e cores escolhidas
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.colorchooser import askcolor
import json



class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.cor_de_fundo = ""
        self.cor_de_frente = "black"
        self.quadro = tk.Frame(self)
        self.cria_barra()
        self.cria_area_de_desenho()
        self.title("Desenho")
        self.geometry("800x600")
        self.cruz = []
        self.cruz.append(self.canvas.create_line((0, 0, 0, 0), dash=[2, 4]))
        self.cruz.append(self.canvas.create_line((0, 0, 0, 0), dash=[2, 4]))
        self.estado = 0
        self.xi = None
        self.yi = None
        self.curr_id = 0
        self.quadro.pack(expand=True, fill=tk.BOTH)
        self.ferramenta = self.canvas.create_line

    def cria_area_de_desenho(self):
        self.trabalho = tk.Frame(self.quadro, height=600)
        self.trabalho.grid(column=1, row=0, sticky=tk.NSEW)
        self.quadro.grid_columnconfigure(1, weight=1)
        self.quadro.grid_rowconfigure(0, weight=1)
        self.canvas = tk.Canvas(self.trabalho, background="white")
        self.canvas.pack(fill=tk.BOTH, expand=True)
        self.canvas.bind("<Motion>", self.mouse_move)
        self.canvas.bind("<Button-1>", self.mouse_click)
        self.canvas.bind("<ButtonRelease-1>", self.mouse_release)
        self.coordenadas = tk.Label(self.trabalho, text="Mova o mouse")
        self.coordenadas.pack(ipadx=10, ipady=10)

    def cria_barra(self):
        self.barra = tk.Frame(self.quadro, width=100, height=600)
        self.blinha = ttk.Button(
            self.barra, text="Linha", padding="10", command=self.ferramenta_linha
        )
        self.blinha.pack()
        self.boval = ttk.Button(
            self.barra, text="Círculo", padding="10", command=self.ferramenta_oval
        )
        self.boval.pack()
        self.bretângulo = ttk.Button(
            self.barra,
            text="Retângulo",
            padding="10",
            command=self.ferramenta_retângulo,
        )
        self.bretângulo.pack()
        bdesfaz = ttk.Button(
            self.barra, text="Desfaz", padding="10", command=self.desfaz
        )
        bdesfaz.pack()
        blimpa = ttk.Button(self.barra, text="Limpa", padding="10", command=self.limpa)
        blimpa.pack()
        self.lfrente = ttk.Label(self.barra, text="Cor de Frente")
        self.lfrente.pack()
        self.bfrente = tk.Button(
            self.barra, text="Cor", command=self.cor_frente, bg=self.cor_de_frente
        )
        self.bfrente.pack(fill="x")
        self.lfundo = ttk.Label(self.barra, text="Cor de Fundo")
        self.lfundo.pack()
        self.bfundo = tk.Button(
            self.barra, text="Transparente", command=self.cor_fundo, bg=None
        )
        self.bfundo.pack(fill="x")
        self.barra.grid(column=0, row=0, sticky=tk.NS)
        self.salvar = tk.Button(
            self.barra,text="Salvar",command=self.salvar_desenho
        )
        self.salvar.pack()
        self.carregar = tk.Button(
            self.barra,text="Carregar Desenho",command=self.abrir_desenho
        )
        self.carregar.pack()
    def desfaz(self):
        if itens := self.canvas.find_withtag("desenho"):
            self.canvas.delete(itens[-1])

    def limpa(self):
        self.canvas.delete("desenho")

    def cor_fundo(self):
        cor = askcolor(title="Cor de fundo")
        self.cor_de_fundo = cor[1] or ""
        self.bfundo.config(
            text="Transparente" if self.cor_de_fundo == "" else "",
            background=self.cor_de_fundo or "SystemButtonFace",
        )

    def cor_frente(self):
        cor = askcolor(title="Cor de frente")
        if cor[1]:
            self.cor_de_frente = cor[1]
            self.bfrente.config(background=self.cor_de_frente)

    def ferramenta_linha(self):
        self.ferramenta = self.canvas.create_line

    def ferramenta_oval(self):
        self.ferramenta = self.canvas.create_oval

    def ferramenta_retângulo(self):
        self.ferramenta = self.canvas.create_rectangle

    def mouse_move(self, event):
        self.coordenadas["text"] = f"Mouse x={event.x} y ={event.y}"
        self.canvas.coords(
            self.cruz[0], event.x, 0, event.x, self.canvas.winfo_height()
        )
        self.canvas.coords(self.cruz[1], 0, event.y, self.canvas.winfo_width(), event.y)
        if self.estado == 1:
            self.canvas.coords(self.curr_id, self.xi, self.yi, event.x, event.y)

    def mouse_click(self, event):
        if self.estado == 0:
            self.xi = event.x
            self.yi = event.y
            self.curr_id = self.ferramenta(
                (self.xi, self.yi, event.x, event.y),
                fill=self.cor_de_frente,
                tags=["desenho"],
            )
            tipo = self.canvas.type(self.curr_id)
            if tipo in ["rectangle", "oval"]:
                self.canvas.itemconfig(
                    self.curr_id,
                    {
                        "outline": self.cor_de_frente,
                        "fill": self.cor_de_fundo,
                    },
                )
            self.estado = 1

    def mouse_release(self, event):
        if self.estado == 1:
            self.estado = 0

    import json # Importe no topo do arquivo

    def salvar_desenho(self, nome_arquivo="desenho.json"):
        dados = []
        for item_id in self.canvas.find_withtag("desenho"):
            tipo = self.canvas.type(item_id)
            coords = self.canvas.coords(item_id)
            fill = self.canvas.itemcget(item_id, "fill")
        
        # Só tenta pegar o 'outline' se o item for um círculo ou retângulo
            if tipo in ["oval", "rectangle"]:
                outline = self.canvas.itemcget(item_id, "outline")
            else:
                 outline = None  # Linhas não têm outline
            
            dados.append({
            "tipo": tipo,
            "coords": coords,
            "fill": fill,
            "outline": outline
        })
    
        with open(nome_arquivo, "w") as f:
            json.dump(dados, f)
        print("Desenho salvo com sucesso!")

    def abrir_desenho(self, nome_arquivo="desenho.json"):
        try:
            with open(nome_arquivo, "r") as f:
                dados = json.load(f)
            
            self.limpa() 
        
            for item in dados:
           
                if item["tipo"] == "line":
                    self.canvas.create_line(item["coords"], fill=item["fill"], tags=["desenho"])
                elif item["tipo"] == "oval":
                    self.canvas.create_oval(item["coords"], fill=item["fill"], outline=item["outline"], tags=["desenho"])
                elif item["tipo"] == "rectangle":
                    self.canvas.create_rectangle(item["coords"], fill=item["fill"], outline=item["outline"], tags=["desenho"])
            print("Desenho carregado!")
        except FileNotFoundError:
            print("Arquivo não encontrado.")
App().mainloop()