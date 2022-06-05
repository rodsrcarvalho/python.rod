import shutil

class Error(Exception):
    pass

class ImputError(Error):
    def _init_(self, message):
        self.message = message

while True:
    try:
        x = int(input('Entre com uma nota de 0 à 10: '))
        print(x)
        if x > 10:
            raise ImputError('Nota tem que ser menor ou igual a 10.')
        elif x < 0:
            raise ImputError('Nota tem que ser maior ou igual a 0.')
        break
    except ValueError:
        print('Valor Inválido. Lance apenas números.')
    except ImputError as ex:
        print(ex)