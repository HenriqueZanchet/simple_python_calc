# calculadora.py

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
    print(f"A soma de {num1}, {num2} e {sum3} é: {resultado}")

if __name__ == "__main__":
    main()
