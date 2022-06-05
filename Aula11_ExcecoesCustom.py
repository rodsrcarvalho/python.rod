
lista = [1, 10]
try:
    divisao = 10 / 1
    numero = lista[1]

except ZeroDivisionError:
    print('Não é possível realizar uma divisão por 0')
except ArithmeticError:
    print('Houve um erro ao realizar uma operação aritimética')
except IndexError:
    print('Erro ao acessar um índice inválido da lista')
except BaseException as ex:
    print('Erro encontrado: {}'.format(ex))
else:
    print('Executou programa sem erro')
finally:
    print('Sempre executa')
    print('Fechando arquivo')

