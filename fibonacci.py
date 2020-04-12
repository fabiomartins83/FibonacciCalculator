# Calculadora para números de Fibonacci
# Desenvolvido por Fábio de Almeida Martins

a, b = 0, 1
x = int(input("CALCULADORA FIBONACCI. Digite o número limite: "))
print("Calculando os números de Fibonacci até",x,": ")
while a < x:
    print(a, end=" ")
    a, b = b, a+b
