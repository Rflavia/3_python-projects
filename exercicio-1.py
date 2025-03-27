# 1 - Loops em Python

numero = int(input("Digite um número inteiro: "))


soma = 0


print(f"Números de 1 até {numero}:")
for i in range(1, numero + 1):
    print(i)
    soma += i

print(f"A soma de todos os números de 1 até {numero} é: {soma}")


# 2
def numeros_primos(n):
    primos = []
    for num in range(2, n + 1):
        eh_primo = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                eh_primo = False
                break
        if eh_primo:
            primos.append(num)
    return primos


n = 50
print(f"Os números primos até {n} são: {numeros_primos(n)}")



# 3
def transposta(matriz):
    
    transposta_matriz = []
    for j in range(len(matriz[0])): 
        nova_linha = []
        for i in range(len(matriz)):  
            nova_linha.append(matriz[i][j])
        transposta_matriz.append(nova_linha)
    return transposta_matriz

def verificar_simetria(matriz):
   
    if len(matriz) != len(matriz[0]):
        return "Matriz não Simétrica"

    transposta_matriz = transposta(matriz)
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j] != transposta_matriz[i][j]:
                return "Matriz não Simétrica"
    return "Matriz Simétrica"

matriz = [
    [1, 2, 3],
    [2, 4, 5],
    [3, 5, 6]
]

print("Matriz Original:")
for linha in matriz:
    print(linha)

print("\nMatriz Transposta:")
matriz_transposta = transposta(matriz)
for linha in matriz_transposta:
    print(linha)

print("\nResultado da verificação de simetria:")
print(verificar_simetria(matriz))




