import dataclasses


# MODEL


@dataclasses.dataclass
class Board:
    board = list()

    @staticmethod
    def check_win(board):
        win_coord = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
        for each in win_coord:
            if board[each[0]] == board[each[1]] == board[each[2]]:
                return board[each[0]]
        return False


# VIEW


class View:
    def draw_board(self, board):
        print("-" * 13)
        for i in range(3):
            print("|", board[0 + i * 3], "|", board[1 + i * 3], "|", board[2 + i * 3], "|")
            print("-" * 13)



# Controller

@dataclasses.dataclass
class Controller:
    def take_input(self, player_token, board):
        valid = False
        while not valid:
            player_answer = input("Куда поставим " + player_token + "? ")
            try:
                player_answer = int(player_answer)
            except:
                print("Некорректный ввод. Вы уверены, что ввели число?")
                continue
            if 1 <= player_answer <= 9:
                if str(board[player_answer - 1]) not in "XO":
                    board[player_answer - 1] = player_token
                    valid = True
                else:
                    print("Эта клеточка уже занята")
            else:
                print("Некорректный ввод. Введите число от 1 до 9 чтобы походить.")


if __name__ == '__main__':
    c = Controller()
    view = View()
    counter = 0
    b = list(range(1, 10))
    win = False
    while not win:
        view.draw_board(b)
        if counter % 2 == 0:
            c.take_input("X", b)
        else:
            c.take_input("O", b)
        counter += 1
        if counter > 4:
            tmp = Board.check_win(b)
            if tmp:
                print(tmp, "Выиграл!")
                win = True
                break
            if counter == 9:
                print("Ничья!")
                break

