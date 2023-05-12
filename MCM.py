def calcular_mcm(a, b):
    max_val = max(a, b)
    mcm = max_val
    while True:
        if mcm % a == 0 and mcm % b == 0:
            break
        mcm += max_val
    return mcm
num1 = int(input(" "))
num2 = int(input(" "))
resultado = calcular_mcm(num1, num2)
print(resultado)
