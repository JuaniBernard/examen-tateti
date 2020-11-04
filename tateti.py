class TaTeTi():
    def __init__(self, board={'1.1': '1.1', '1.2': '1.2', '1.3': '1.3',
                              '2.1': '2.1', '2.2': '2.2', '2.3': '2.3',
                              '3.1': '3.1', '3.2': '3.2', '3.3': '3.3'},
                 piece='', valid=['1.1', '1.2', '1.3',
                                  '2.1', '2.2', '2.3',
                                  '3.1', '3.2', '3.3']):
        self.board = board
        self.piece = piece
        self.valid = valid

    def __str__(self):
        tab = (self.board['1.1'] + '|' + self.board['1.2'] + '|' +
               self.board['1.3'] + '\n' + '---+---+---'+'\n' +
               self.board['2.1'] + '|' + self.board['2.2'] + '|' +
               self.board['2.3'] + '\n' + '---+---+---'+'\n' +
               self.board['3.1'] + '|' + self.board['3.2']+'|' +
               self.board['3.3'])
        return tab

    def input_position(self):
        p = 0
        while p == 0:
            pos = input('\n Ingrese alguna posición: ')
            if pos in self.valid:
                self.valid.remove('{}'.format(pos))
                p = 1
                return pos

    def game(self):
        print(self)
        while not self.win() and len(self.valid) > 0:
            self.board[self.input_position()] = ' ' + self.piece + ' '
            print(self)
            winner = self.piece
            self.piece = 'o' if self.piece == 'x' else 'x'
        if len(self.valid) == 0:
            winner = 'Ninguno'
        return winner

    def win(self):
        # filas
        if self.board['1.1'] == self.board['1.2'] and\
             self.board['1.2'] == self.board['1.3']:
            return True
        elif self.board['2.1'] == self.board['2.2'] and\
                self.board['2.2'] == self.board['2.3']:
            return True
        elif self.board['3.1'] == self.board['3.2'] and\
                self.board['3.2'] == self.board['3.3']:
            return True
        # columnas
        elif self.board['1.1'] == self.board['2.1'] and\
                self.board['2.1'] == self.board['3.1']:
            return True
        elif self.board['1.2'] == self.board['2.2'] and\
                self.board['2.2'] == self.board['3.2']:
            return True
        elif self.board['1.3'] == self.board['2.3'] and\
                self.board['2.3'] == self.board['3.3']:
            return True
        # diagonales
        elif self.board['1.1'] == self.board['2.2'] and\
                self.board['2.2'] == self.board['3.3']:
            return True
        elif self.board['1.3'] == self.board['2.2'] and\
                self.board['2.2'] == self.board['3.1']:
            return True
        else:
            return False


if __name__ == '__main__':
    game = TaTeTi()

    print('Ganó ' + game.game())
