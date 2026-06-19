#Este programa será util no exercicio 12.1
entrada = "ABC431DEF901c431203FXEW9"
saída = []
número = []
for caractere in entrada:
    if "0" <= caractere <= "9":
        if not número:
            saída.append(número)
        número += caractere
    elif número:
        número = []
for encontrado in saída:
    print("".join(encontrado))