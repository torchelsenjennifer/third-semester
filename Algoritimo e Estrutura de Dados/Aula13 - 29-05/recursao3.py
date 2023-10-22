def fatorial(num):
    if num == 0:
        return 1
    else:
        retorno = fatorial(num - 1)
        return num * retorno

fat = fatorial(5)
print(f"Fatorial de 5: {fat}")