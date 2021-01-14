from atividade_3 import Quadrilatero


class Teste(Quadrilatero):
    def __init__(self, x, y, P1x, P1y, P2x, P2y):
        super().__init__(x, y, P1x, P1y, P2x, P2y)

    def mostrateste(self):

        print('\nPonto: ({}, {})'.format(self.getX(), self.getY()))
        print('Quadrante: {}'.format(self.qualQuadrante()))

        if self.P1x < self.P2x and self.P1y > self.P2y:
            print('\nP1: {}'.format(self.P1))
            print('P2: {}'.format(self.P2))

        else:
            print('Não é possivel formar um Quadrilatero')
        print(self.contidoEmQ())


if __name__ == '__main__':
    x = input('X: ')
    y = input('Y: ')
    P1x = input('P1x: ')
    P1y = input('P1y: ')
    P2x = input('P2x: ')
    P2y = input('P2y: ')

    a = Teste(x, y, P1x, P1y, P2x, P2y)
    a.mostrateste()
