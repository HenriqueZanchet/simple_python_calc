# calculadora.py
def subtrair(a, b, c):
    """Retorna a subtração de três números."""
    return a - b - c


def somar3(a, b, c):
    """Retorna a soma de dois números."""
    return a + b + c

def main():
    """Função principal do programa."""
    print("Bem-vindo à Calculadora em Python! Vamos somar dois números.")

    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    num3 = float(input("Digite o terceiro número: "))
    
    resultado = somar3(num1, num2, num3)
    print(f"A soma de {num1}, {num2} e {num3} é: {resultado}")
    
    print("Agora vamos subtrair dois números.")
    num4 = float(input("Digite o primeiro número: "))
    num5 = float(input("Digite o segundo número: "))
    num6 = float(input("Digite o terceiro número: "))
    resultado = subtrair(num4, num5, num6)
    print(f"A subtração de {num4} e {num5} e {num6} é: {resultado}")

    print("Fim da aplicação.")

if __name__ == "__main__":
    main()
