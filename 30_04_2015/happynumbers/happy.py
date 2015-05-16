def happy(n):
    if n <= 0:
        return False

    resultado = n

    if resultado == 1:
        return True
    lista = []
    while resultado != 1:
        lista.append(resultado)  # guarda todos os resultados já encontrados
        resultado = str(resultado)
        soma = 0
        for letra in resultado:
            soma = soma + int(letra) ** 2  # onde a elevação ao quadrado

        resultado = soma

        print(resultado)

        if (resultado in lista):  # isso já estará na lista
            print(str(n) + " não é feliz!")
            return False

    if resultado == 1:
        print(str(n) + " é feliz!")

    return True

lista = [1, 7, 10, 13, 19, 23, 28, 31, 32, 44, 49, 68, 70, 79, 82, 86, 91, 94, 97, 100, 103, 109, 129, 130, 133, 139,
         167, 176, 188, 190, 192, 193, 203, 208, 219, 226, 230, 236, 239, 262, 263, 280, 291, 293, 301, 302, 310, 313,
         319, 320, 326, 329, 331, 338, 356, 362, 365, 367, 368, 376, 379, 383, 386, 391, 392, 397, 404, 409, 440, 446,
         464, 469, 478, 487, 490, 496]

numeros = range(lista[-1])
nao_felizes = [n for n in numeros if n not in lista]

assert all([happy2(num) for num in lista])
assert not all([happy2(num) for num in nao_felizes])
