#Modifique o Programa 9.8 para utilizar o elemento p em vez de h2 nos filmes
filmes = {
    "drama": ["Cidadão Kane", "O Poderoso Chefão"],
    "comédia": ["Tempos Modernos", "American Pie", "Dr. Dolittle"],
    "policial": ["Chuva Negra", "Desejo de Matar", "Difícil de Matar"],
    "guerra": ["Rambo", "Platoon", "Tora!Tora!Tora!"],
}
with open("pt2ex9.29.html", "w", encoding="utf-8") as página:
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
        for e in v:
            página.write(f"<p>{e}</p>\n")
    página.write("</body></html>")