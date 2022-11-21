# NodaPoint Точки на игровом поле с координатами X - номер строки Y - номер стобца
import time
from random import random, choices
from random import randint


class AllException(Exception):
    """Все исключения"""
    pass


class OutException(AllException):
    """Исключение при попадании за пределы поля"""

    def __str__(self):
        return "Стреляй точнее! Повтор!"


class BusyException(AllException):
    """Исключение при введении координат повторно"""

    def __str__(self):
        return "Уже было"


class ShipException(AllException):
    pass


class NodalPoint:
    """"Точки на игровом поле с координатами X - номер строки Y - номер стобца"""

    def __init__(self, x=None, y=None):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return f"({self.x}, {self.y})"


class Ship:
    """Корабль (началo (координаты(строка_X,столбеу_Y, длина, ориентация)"""

    def __init__(self, beginning, len_ship, orient):
        self.beginning = beginning
        self.len_ship = len_ship
        self.orient = orient
        self.lives = len_ship

    @property
    def ship_points(self):

        points = []
        for i in range(self.len_ship):
            point_x = self.beginning.x
            point_y = self.beginning.y

            if self.orient == 0:
                point_x += i

            elif self.orient == 1:
                point_y += i

            points.append(NodalPoint(point_x, point_y))

        return points

    def killed(self, shot):
        """Попадание в корабль"""
        return shot in self.ship_points


class GameArea:
    """Игровое поле ячеек в шесть сток X и шесть столбцов Y"""

    def __init__(self, hid=False):
        self.hid = hid
        self.count = 0
        self.field = [["-"] * 6 for _ in range(6)]
        self.busy = []
        self.ships = []

    def add_ship(self, ship):

        for p in ship.ship_points:
            if self.out_game_area(p) or p in self.busy:
                raise ShipException()
        for p in ship.ship_points:
            self.field[p.x][p.y] = chr(174)
            self.busy.append(p)

        self.ships.append(ship)
        self.contour(ship)

    def contour(self, ship, verb=False):
        dead = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1), (0, 0), (0, 1),
            (1, -1), (1, 0), (1, 1)
        ]
        for p in ship.ship_points:
            for px, py in dead:
                current = NodalPoint(p.x + px, p.y + py)
                if not (self.out_game_area(current)) and current not in self.busy:
                    if verb:
                        self.field[current.x][current.y] = "v"
                    self.busy.append(current)

    def __str__(self):
        res = ""
        res += "      1  2  3  4  5  6  "
        for i, row in enumerate(self.field):
            res += f"\n    {i + 1} " + "  ".join(row)

        if self.hid:
            res = res.replace(chr(174), "-")
        return res

    def out_game_area(self, p):
        return not ((0 <= p.x < 6) and (0 <= p.y < 6))

    def shot(self, p):
        if self.out_game_area(p):
            raise OutException()

        if p in self.busy:
            raise BusyException()

        self.busy.append(p)

        for ship in self.ships:
            if p in ship.ship_points:
                ship.lives -= 1
                self.field[p.x][p.y] = "\033[31mX\033[0m"
                if ship.lives == 0:
                    self.count += 1
                    self.contour(ship, verb=True)
                    print("Уничтожен!")
                    time.sleep(4)
                    return False
                else:
                    print("Ранен!")
                    time.sleep(4)
                    return True

        self.field[p.x][p.y] = "v"
        print("Мимо!")
        time.sleep(4)
        return False

    def begin(self):
        self.busy = []


class Player:
    """Игровое поле игрока"""

    def __init__(self, board, enemy):
        self.board = board
        self.enemy = enemy

    def ask(self):
        raise NotImplementedError()

    def move(self):
        while True:
            try:
                target = self.ask()
                repeat = self.enemy.shot(target)
                return repeat
            except AllException as e:
                print(e)


class AutoMove(Player):
    def ask(self):
        points = [NodalPoint]
        board = GameArea()
        for i in range(len(board.field)):
            for j in range(len(board.field[i])):
                if board.field[i][j] == "-":
                    points.append(NodalPoint(x=i, y=j))
        ch = NodalPoint()
        c = choices(points, k=1)
        [(ch)] = c
        print(f"Компьютер сходил: {ch.x + 1} {ch.y + 1}")
        time.sleep(2)
        return ch


class User(Player):

    def ask(self):
        while True:
            cords = input("Ваш ход: ").split()

            if len(cords) != 2:
                print(" Нужно ввести 2 координаты! ")
                continue

            x, y = cords

            if not (x.isdigit()) or not (y.isdigit()):
                print(" Введите числа! ")
                continue

            x, y = int(x), int(y)
            print(f"Ты сходил: {x} {y}")
            time.sleep(2)
            return NodalPoint(x - 1, y - 1)


class Game:
    def __init__(self):
        pl = self.random_board()
        co = self.random_board()
        co.hid = True

        self.ai = AutoMove(co, pl)
        self.us = User(pl, co)

    def random_board(self):
        board = None
        while board is None:
            board = self.random_ships()
        return board

    def random_ships(self):
        lens = [3, 2, 2, 1, 1, 1, 1]
        board = GameArea()
        attempts = 0
        for l in lens:
            while True:
                attempts += 1
                if attempts > 1000:
                    return None
                ship = Ship(NodalPoint(randint(0, 6), randint(0, 6)), l, randint(0, 1))
                try:
                    board.add_ship(ship)
                    break
                except ShipException:
                    pass
        board.begin()
        return board

    def greet(self):
        print("_____________________________")
        print(" первое число - номер строки  ")
        print(" второе число - номер столбца ")

    def loop(self):
        num = 0
        while True:
            print("-" * 20)
            print("Поле пользователя:")
            print(self.us.board)
            print("-" * 20)
            print("Поле компьютера:")
            print(self.ai.board)
            if num % 2 == 0:
                print("-" * 25)
                print("Сделай свой  ход !")
                print("Строка, пробел, столбец")
                repeat = self.us.move()
            else:
                print("-" * 25)
                print("Ход компьютера!")
                repeat = self.ai.move()
            if repeat:
                num -= 1

            if self.ai.board.count == 7:
                print("-" * 25)
                print("Ты выиграл!")
                break

            if self.us.board.count == 7:
                print("-" * 25)
                print("Компьютер выиграл!")
                break
            num += 1

    def start(self):
        self.greet()
        self.loop()


g = Game()
g.start()
