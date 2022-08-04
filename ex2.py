#[0.5] Faça uma solução em Python que receba três valores X, Y e Z, verifique se eles podem ser os comprimentos dos lados de um triângulo e, se forem, verifique se é um triângulo equilátero, isósceles ou escaleno. Se eles não formarem um triângulo, escreva uma mensagem. Considere que:
 
a = float(input("Digite o primeiro lado: "))
b = float(input("Digite o segundo lado: "))
c = float(input("Digite o terceiro lado: "))
if a + b < c or a + c < b or b + c < a or a <= 0 or b <= 0 or c <= 0:
        print("Não forma um triângulo")
else:
    if a == b == c:
        print("Este triângulo é equilátero")
    else:
        if a == b or a== c or b == c:
            print("Este triângulo é isósceles")
        else:
            print("Este triângulo é escaleno")