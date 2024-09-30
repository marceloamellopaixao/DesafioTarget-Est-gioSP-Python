def fibonacci(n):
    a, b = 0, 1
    fib_sequence = [a, b]
    while b <= n:
        a, b = b, a + b
        fib_sequence.append(b)
    return fib_sequence[:-1]

def confirmar_fibonacci(num):
    fib_seq = fibonacci(num)
    if num in fib_seq:
        return f"O número {num}, pertence à sequência de Fibonacci."
    else:
        return f"O número {num}, não pertence à sequência de Fibonacci."


numero = int(input('Digite um número para verificar se pertence à sequência de Fibonacci: '))
print()
while numero < 0:
    numero = int(input('Digite um número inteiro e positivo para verificar se pertence à sequência de Fibonacci: '))
    print()

print(confirmar_fibonacci(numero))