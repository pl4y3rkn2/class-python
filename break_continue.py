def run():
    # for contador in range(1000):
    #     if contador % 2 != 0:
    #         continue  # todo lo q esta despues de continio no se ejacuta
    #     print(contador)

    # for i in range(10000):
    #     print(i)
    #     if i == 5678:
    #         break #para cerra el ciclo si se cumple el if

    texto = input('Escribe un texto: ')
    for letra in texto:
        if letra == 'o':
            break #se cortara si llega a la letra o
        print(letra)


if __name__ == '__main__':
    run()
