#Altere o programa para ler a última agenda lida ou gravada ao inicializar. 
# Dica: utilize outro arquivo para armazenar o nome.
agenda = []
alterada = False

def pede_nome():
    return input("Nome: ")


def pede_telefone():
    return input("Telefone: ")


def mostra_dados(nome, telefone):
    print(f"Nome: {nome} Telefone: {telefone}")


def pede_nome_arquivo():
    return input("Nome do arquivo: ")


def pesquisa(nome):
    mnome = nome.lower()
    for p, e in enumerate(agenda):
        if e[0].lower() == mnome:
            return p
    return None


def novo():
    global agenda,alterada
    nome = pede_nome()
    telefone = pede_telefone()
    agenda.append([nome, telefone])
    alterada = True

def apaga():
    global agenda, alterada
    nome = pede_nome()
    p = pesquisa(nome)
    if p is not None:
        confirmação = input("deseja apagar a agenda?, digite 's' se sim").strip().lower()
        if confirmação == "s":
            del agenda[p]
            alterada = True
        else:
            print("nada foi apagado")
        
    else:
        print("Nome não encontrado.")


def altera():
    global  alterada
    p = pesquisa(pede_nome())
    if p is not None:
        nome = agenda[p][0]
        telefone = agenda[p][1]
        print("Encontrado:")
        mostra_dados(nome, telefone)
        confirmação = input("deseja alterar?, digite 's' se sim").strip().lower()
        if confirmação == "s":
            nome = pede_nome()
            telefone = pede_telefone()
            agenda[p] = [nome, telefone]
            alterada = True 
        else:
            print("nada foi alterado")
    else:
        print("Nome não encontrado.")


def lista():
    print("\nAgenda\n\n------")
    for e in agenda:
        mostra_dados(e[0], e[1])
    print("------\n")


def lê():
    global agenda
    nome_arquivo = pede_nome_arquivo()
    with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
        agenda = []
        for linha in arquivo.readlines():
            nome, telefone = linha.strip().split("#")
            agenda.append([nome, telefone])
    with open("pt2ex9.23.txt","w") as pt2:
        pt2.write(nome_arquivo)

def grava():
    global alterada, agenda
    nome_arquivo = pede_nome_arquivo()
    with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
        for e in agenda:
            arquivo.write(f"{e[0]}#{e[1]}\n")
        alterada = False
    with open("pt2ex9.23.txt","w") as pt2:
        pt2.write(nome_arquivo)

def valida_faixa_inteiro(pergunta, início, fim):
    while True:
        try:
            valor = int(input(pergunta))
            if início <= valor <= fim:
                return valor
        except ValueError:
            print(f"Valor inválido, favor digitar entre {início} e {fim}")


def ordernar_lista():
    global alterada
    agenda_ordenada = sorted(agenda)
    print(f"A lista ordenada fica como {agenda_ordenada}")
    alterada = True


def verificar_lista():
    global alterada
    if alterada == True:
        return True
    else:
        return False

def menu():
    print("""
  1 – Novo
  2 – Altera
  3 – Apaga
  4 – Lista
  5 – Grava
  6 – Lê
  7 – Ordena a lista
  8 – Verificar a alteração da agenda
  0 – Sai
""")
    print(f"A alteração da lista é {alterada}")
    return valida_faixa_inteiro("Escolha uma opção: ", 0, 8)
try:
    with open ("pt2ex9.23.txt","r", encoding="utf-8") as ponte:
        with open ("pt3ex9.23.txt","r",encoding="utf-8") as agds:
            agenda = []
            for linha in agds.readlines():
                nome, telefone = linha.strip().split("#")
                agenda.append([nome, telefone])
except FileNotFoundError:
    print("Não houve um Inicializador encontrado, por favor, faça sua agenda")

while opção := menu():
    if opção == 0:
        break
    elif opção == 1:
        novo()
    elif opção == 2:
        altera()
    elif opção == 3:
        apaga()
    elif opção == 4:
        lista()
    elif opção == 5:
        grava()
    elif opção == 6:
        lê()
    elif opção == 7:
        ordernar_lista()
    elif opção == 8:
        verificar_lista()