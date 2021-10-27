# 1 - imports - bibliotecas
import pytest
# 2 - class - classe

# 3 - definitions - definições = metódos e funções
def print_hi(name):
    print(f'Oi, {name}')

def somar(numero1, numero2):
    return numero1 + numero2

def subtrair(numero1, numero2):
    return numero1 - numero2

def multiplicar(numero1, numero2):
    return numero1 * numero2

def dividir(numero1, numero2):
    if numero2 != 0:
        return numero1 / numero2
    else:
        return 'Não dividirás por zero'

# Testes Unitários / teste de unidade

    # teste da função somar
def test_somar_didatico():
    # 1 - Configura / Prepara
    numero1 = 8 # input / entrada
    numero2 = 5 # input / entrada
    resultado_esperado = 13 # output / saida

    # 2 - Executa
    resultado_atual = somar(numero1, numero2)

    # 3 - Valida
    assert resultado_atual == resultado_esperado

@pytest.mark.parametrize('numero1,numero2,resultado',[
    #valores
    (5, 4, 9),      # teste 1
    (3, 2, 5),      # teste 2
    (10, 6, 16),    # teste 3
])

def test_somar(numero1, numero2, resultado):
    assert somar(numero1, numero2) == resultado

def test_somar_resultado_negativo():
    assert somar(-1000,-2000) == -3000

def test_subtrair():
    assert subtrair(4,5) == -1

def test_multiplicar():
    assert multiplicar(3,7) == 21

def test_dividir():
    assert dividir(8,4) == 2

# Dia 1 : 100 testes : 0 passaram
# Dia 2 : 100 testes : 5 passaram
# Dia 3 : 100 testes : 15 passaram
# Dia 4 : 100 testes : 30 passaram

#TDD : Desenvolvimento Direcionado pelo Teste
# - Criar o esqueleto de classes, funçôes e métodos logo no início da Spprint
# - Criar pelo menos um teste (feliz) para todas as funções e métodos
# - Executar todos os testes unitários diariamente para medir o progresso

if __name__ == '__main__':
    print_hi('Iasmin')

    # somar dois números
    resultado = somar(4, 2)
    print(f'O resultado da soma: {resultado}')

    # subtrair dois números
    resultado = subtrair(5,3)
    print(f'O resultado da subtração: {resultado}')

    # multiplicar dois números
    resultado = multiplicar(2,4)
    print(f'O resultado da multiplicação: {resultado}')

    # divisão
    resultado = dividir(9,0)
    print(f'O resultado da multiplicação: {resultado}')

