# calculadora.py

def somar(a, b):
    """Retorna a soma de dois números."""
    return a + b

def main():
    """Função principal do programa."""
    print("Bem-vindo à Calculadora em Python! Vamos somar dois números.")

    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    resultado = somar(num1, num2)
    print(f"A soma de {num1} e {num2} é: {resultado}")

if __name__ == "__main__":
    main()