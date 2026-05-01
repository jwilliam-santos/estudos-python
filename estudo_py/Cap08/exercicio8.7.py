#Defina uma função recursiva que calcule o maior divisor comum (M.D.C.) entre dois números a e b, emque a > b.
#Ver representação no livro.
def mdc(a,b):
    if b == 0:
        return a
    else:
        return mdc(b, a % b )
print(mdc(48,18))