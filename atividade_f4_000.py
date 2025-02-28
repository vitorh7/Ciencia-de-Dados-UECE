# Criar funções matemáticas
# Área de um quadrado
def area_quadrado(lado):
    return lado * lado

# Área de um retângulo
def area_retangulo(base, altura):
    return base * altura

# Guardando valores em variáveis
l = int(input("Digite o valor do lado do quadrado: "))
b = int(input("Digite o valor da base do retângulo: "))
a = int(input("Digite o valor da altura do retângulo: "))

# Exibindo os resultados
print("Área do quadrado:", area_quadrado(l))
print("Área do retângulo:", area_retangulo(b, a))
