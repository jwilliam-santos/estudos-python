#Modifique o programa anterior e grave a imagem no formato SVG.
#O formato SVG é um arquivo texto, que segue um formato bem definido.
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.colorchooser import askcolor
import xml.etree.ElementTree as ET



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
            self.barra,text="Carregar Desenho",command=self.abrir_svg
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



    def salvar_desenho(self, nome_arquivo="desenho.svg"):
        with open(nome_arquivo, "w") as f:
            # Cabeçalho padrão do arquivo SVG
            f.write('<svg xmlns="http://www.w3.org/2000/svg" width="800" height="600">\n')
            
            for item_id in self.canvas.find_withtag("desenho"):
                tipo = self.canvas.type(item_id)
                coords = self.canvas.coords(item_id)
                fill = self.canvas.itemcget(item_id, "fill")
                
                # Tenta ler o outline, mas se der erro (caso de linhas), define como vazio
                try:
                    outline = self.canvas.itemcget(item_id, "outline")
                except:
                    outline = ""

                if tipo == "line":
                    f.write(f'  <line x1="{coords[0]}" y1="{coords[1]}" x2="{coords[2]}" y2="{coords[3]}" stroke="{fill}" />\n')
                
                elif tipo == "rectangle":
                    w = coords[2] - coords[0]
                    h = coords[3] - coords[1]
                    f.write(f'  <rect x="{coords[0]}" y="{coords[1]}" width="{w}" height="{h}" fill="{fill}" stroke="{outline}" />\n')
                
                elif tipo == "oval":
                    cx = (coords[0] + coords[2]) / 2
                    cy = (coords[1] + coords[3]) / 2
                    rx = (coords[2] - coords[0]) / 2
                    ry = (coords[3] - coords[1]) / 2
                    f.write(f'  <ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" fill="{fill}" stroke="{outline}" />\n')
            
            f.write('</svg>')
        print("Salvo em SVG com sucesso!")

    def abrir_svg(self, nome_arquivo="desenho.svg"):
        try:
            tree = ET.parse(nome_arquivo)
            root = tree.getroot()
            self.limpa() # Limpa o canvas antes de carregar o novo

            for child in root:
            # child.tag no SVG será algo como '{http://www.w3.org/2000/svg}line'
            # Usamos .split('}') para pegar só 'line', 'rect' ou 'ellipse'
                tag = child.tag.split('}')[-1]

                if tag == "line":
                    x1 = float(child.attrib["x1"])
                    y1 = float(child.attrib["y1"])
                    x2 = float(child.attrib["x2"])
                    y2 = float(child.attrib["y2"])
                    fill = child.attrib.get("stroke")
                    self.canvas.create_line(x1, y1, x2, y2, fill=fill, tags=["desenho"])

                elif tag == "rect":
                     x = float(child.attrib["x"])
                     y = float(child.attrib["y"])
                     w = float(child.attrib["width"])
                     h = float(child.attrib["height"])
                     fill = child.attrib.get("fill")
                     stroke = child.attrib.get("stroke")
                     self.canvas.create_rectangle(x, y, x + w, y + h, fill=fill, outline=stroke, tags=["desenho"])

                elif tag == "ellipse":
                    cx = float(child.attrib["cx"])
                    cy = float(child.attrib["cy"])
                    rx = float(child.attrib["rx"])
                    ry = float(child.attrib["ry"])
                    fill = child.attrib.get("fill")
                    stroke = child.attrib.get("stroke")
                # Converte de cx, cy, rx, ry para coordenadas do tkinter (x1, y1, x2, y2)
                    self.canvas.create_oval(cx - rx, cy - ry, cx + rx, cy + ry, fill=fill, outline=stroke, tags=["desenho"])
        
            print("SVG carregado com sucesso!")
        except Exception as e:
            print(f"Erro ao abrir arquivo: {e}")
App().mainloop()