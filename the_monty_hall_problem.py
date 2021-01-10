import random 

# ================================  classes

class Door:
    """ Дверь
    Имеет свой номер и спрятанный за ней приз"""

    def __init__(self, number):

        self.number = number        # просто номер двери: 1, 2 или 3
        self.prize = "Undefined"           # наименование приза: "Car" ..
        self.prize_int = None       # числовое представление приза, 1 или 0

    def __repr__(self):
        return str(self.prize)

class Showmen:
    """Родительский класс шоуменов"""
    def __init__(self):
        self.car_place = None  # все шоумены будут знать номер двери, за которой будет а/м

class Director(Showmen):
    """Режиссер.
    Помещает призы за двери, говорит ведущему, за какой дверью какой приз.
    Заставляет повторять сцену, если плохо снято )."""

    def __init__(self):
        super().__init__()

    def place_prize(self, our_wall):
        # случайно определим номер, за какой будет а/м, и пусть режиссер его запомнит
        self.car_place = random.randint(1, 3)
        # теперь поместим за дверь с выбранным номером а/м, за другие - коз ).
        for n in range(1,4,1):
            if n == self.car_place:
                our_wall[n].prize = "Car"
                our_wall[n].prize_int = 1
            else:
                our_wall[n].prize = "Donkey"
                our_wall[n].prize_int = 0

    def inform(self, alien):
        # сообщим ведущему, где а/м
        alien.car_place = self.car_place


class Host(Showmen):
    """Ведущий, руководит шоу.
    знает, где автомобиль, говорит ему об этом режиссер
    предлагает выбрать или сменить дверь, а также открывает"""
    def __init__(self):
        super().__init__()


class Player:         # ============================================ class Player  - не идет. отладка в testMHP3
    """Игрок. Выбирает, какую дверь открыть"""
    def __init__(self):
        self.selected_door = None

    def choose_door(self, the_same_door = False):
        # при Ложь по умолчанию всегда выбираем новую дверь
        if not the_same_door:
            seq = [1,2,3]
            # если дверь была ранее выбрана - исключим ее номер из выбора
            if not self.selected_door == None:
                seq.remove(self.selected_door)
            # ну и собственно сам выбор
            self.selected_door = random.choice(seq)
        # при Истина оставляем выбор на старой
        return self.selected_door






class Prize:  # перенесу функционал в дверь
    '''Приз. Может быть, чем угодно, хоть козой, хоть автомобилем
    Помещается за дверь режиссером'''
    name: object
    prize: object
    val: object

    def __init__(self, prize):
        self.name = prize  # str "Car", ..
        self.val = self.vdc[self.name]  # int 0,1

    def __repr__(self):
        return self.number  # str "Car", ..


class Camera:
    '''Камера. Беспристрастно фиксирует происходящее в студии. Может показать все разультаты'''
    pass

# ------------------------------------ body

# создаем двери, присвоим им номера
d1 = Door(1)
d2 = Door(2)
d3 = Door(3)
# все двери находятся в одной стене, коей будет словарь
door_list = [d1, d2, d3]
wall = dict([(x.number, x) for x in door_list])

# создаем режиссера и ведущего
drc = Director()
hst = Host()
# помещаем режиссером за двери А/м и двух коз
drc.place_prize(wall)
# сообщаем ведущему, где а/м
drc.inform(hst)

# - - - - - - - - - - - - - - - - - - output

print(wall)
