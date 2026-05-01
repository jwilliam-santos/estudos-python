#Usando a função mdc definida no exercício anterio.
#Defina uma função para calcular o menor múltiplo comum (M.M.C.) entre dois números.
#mmc(a, b) = |a × b 
#            |------
#            |mdc(a, b) 
# Em que |a × b| pode ser escrito em Python como: abs(a * b).
def mdc(a,b):
    if b == 0:
        return a
    else:
        return mdc(b, a % b )
def mmc(a,b):
    mmc = abs(a*b) / mdc(a,b)
    return mmc
print(mmc(12,20))
print(mmc(5,7))