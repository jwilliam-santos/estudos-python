#Modifique o programa para também controlar a data de aniversário e o email de cada pessoa.
agenda = []
alterada = False

def pede_nome(padrão=""): 
    resposta = input("nome:")
    if resposta == "":
        return padrão
    else:
        return resposta


def pede_telefone(padrão=""): 
    resposta = input("telefone:")
    if resposta == "":
        return padrão
    else:
        return resposta


def pede_email(padrão=""): 
    resposta = input("email:")
    if resposta == "":
        return padrão
    else:
        return resposta


def pede_aniversario(padrão=""): 
    resposta = input("aniversario:")
    if resposta == "":
        return padrão
    else:
        return resposta


def mostra_dados(nome, telefone,email,aniversario): 
    print(f"Nome: {nome} Telefone: {telefone} Email:{email} Aniversario {aniversario} ")
    


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
    if pesquisa(nome)  is not None:
        print("Nome já existente")
        return 
    telefone = pede_telefone()
    email1 = pede_email()
    aniversario2 = pede_aniversario()
    agenda.append([nome, telefone,email1,aniversario2])
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
            email = pede_email()
            aniversario = pede_aniversario()
            agenda[p] = [nome, telefone,email,aniversario]
            alterada = True 
        else:
            print("nada foi alterado")
    else:
        print("Nome não encontrado.")


def lista(): 
    print("\nAgenda\n\n------")
    for e in agenda:
        mostra_dados(e[0], e[1],e[2],e[3])
    print("------\n")


def lê(): 
    global agenda,email,aniversario
    nome_arquivo = pede_nome_arquivo()
    with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
        agenda = []
        for linha in arquivo.readlines():
            nome, telefone,email,aniversario = linha.strip().split("#")
            agenda.append([nome, telefone,email,aniversario])
    with open("pt2ex9.23.txt","w") as pt2:
        pt2.write(nome_arquivo)

def grava(): #
    global alterada, agenda
    nome_arquivo = pede_nome_arquivo()
    with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
        for e in agenda:
            arquivo.write(f"{e[0]}#{e[1]}#{e[2]}#{e[3]}\n")
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
    print(agenda) 
    return valida_faixa_inteiro("Escolha uma opção: ", 0, 8)
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
    