# 1 manipulação de listas em python

def numeros_primos(lista):
    def eh_primo(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    return [num for num in lista if eh_primo(num)]

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(numeros_primos(lista))

# 2

def concatenar_alternadamente(lista1, lista2):
    return [x for pair in zip(lista1, lista2) for x in pair]

lista1 = [1, 3, 5]
lista2 = [2, 4, 6]

print(concatenar_alternadamente(lista1, lista2))





