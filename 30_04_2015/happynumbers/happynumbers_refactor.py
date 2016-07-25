def soma_dos_quadrados(numero):
    minhastring = str(numero)
    list = []
    for digito in minhastring:
        list.append(int(digito) ** 2)
    return sum(list)

def happy(numero):
    result = numero
    box = []
    while result != 1 and result not in box:
        box.append(result)
        result = somadosquadrados(result)
    return result == 1

lista = [1, 7, 10, 13, 19, 23, 28, 31, 32, 44, 49, 68, 70, 79, 82, 86, 91, 94, 97, 100, 103, 109, 129, 130, 133, 139,
         167, 176, 188, 190, 192, 193, 203, 208, 219, 226, 230, 236, 239, 262, 263, 280, 291, 293, 301, 302, 310, 313,
         319, 320, 326, 329, 331, 338, 356, 362, 365, 367, 368, 376, 379, 383, 386, 391, 392, 397, 404, 409, 440, 446,
         464, 469, 478, 487, 490, 496]

numeros = range(lista[-1])
nao_felizes = [n for n in numeros if n not in lista]

assert all([happy(num) for num in lista])
assert not all([happy(num) for num in nao_felizes])
