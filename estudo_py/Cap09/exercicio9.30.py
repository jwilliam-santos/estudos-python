#Modifique o Programa 9.8 para gerar uma lista HTML, usando os elementos ul e li.
#Todos os elementos da lista devem estar dentro do elemento ul, e cada item dentro de um elemento li.
#Exemplo:
#<ul><li>Item1</li><li>Item2</li><li>Item3</li></ul>
filmes = {
    "drama": ["Cidadão Kane", "O Poderoso Chefão"],
    "comédia": ["Tempos Modernos", "American Pie", "Dr. Dolittle"],
    "policial": ["Chuva Negra", "Desejo de Matar", "Difícil de Matar"],
    "guerra": ["Rambo", "Platoon", "Tora!Tora!Tora!"],
}
with open("pt2ex9.30.html", "w", encoding="utf-8") as página:
    página.write("""
<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<title>Filmes</title>
</head>
<body>
""")
    for c, v in filmes.items():
        página.write(f"<h1>{c}</h1>\n")
        página.write("<ul>\n")
        for e in v:
            página.write(f"<ul><li>{e}</li>\n")
            página.write("</ul>\n")
    página.write("</body></html>")
