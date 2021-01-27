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
        for n in range(1,4,1): # тут достаточно делать выбор просто из трех, этим можно пренебречь
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


class Player:
    """Игрок. Выбирает, какую дверь открыть"""
    def __init__(self):
        self.selected_door = None

    def choose_door(self,attempt, the_same_door = False):
        # далее поубирать лишние ретены
        main_seq = [1, 2, 3]
        seq = [x for x in range (main_seq[0],main_seq[-1]*100+1,1)]
        # при первом выборе выбираем любую вообще
        if attempt == 1:
            self.selected_door = self.accuracy(random.choice(seq))
            return self.selected_door
        # при втором выборе: зависит выбирать ли ту же самую дверь
        if attempt == 2:
            # если ту же самую
            if the_same_door:
                return self.selected_door
            # если надо другую
            else:
                seq.remove(self.selected_door)  # ; print(seq)
                self.selected_door = self.accuracy(random.choice(seq))
                return self.selected_door
    @staticmethod
    def accuracy(got_num):
        if got_num > 200:
            return 3
        elif got_num > 100:
            return 2
        else:
            return 1
    @staticmethod #  короче из (которая будет) 1 созлать последовательность 1- 100, далее из 2х - 2-100
    def seq(main_seq):
        for elem in seq:
            seq_cur = # детальная отладка в третьем тестовом



class Prize:  # перенести функционал в дверь
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
    def __init__(self):
        self.first_choice = None
        self.second_choice = None
    def record(self,choice):
        self.first_choice = choice

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
camera = Camera()
plr = Player()
# помещаем режиссером за двери А/м и двух коз
drc.place_prize(wall)
# сообщаем ведущему, где а/м
drc.inform(hst)
# ведущий должен спросить у грока, что он выберет, и камера должна это зафиксировать

---------------------------проектируенм дальнейшшее поведение товарищей в студии

camera.record(hst.ask(player.choose_door(1, thesame = false)))) ^  1 - номер попытки/ответа, то_же - вибыраем ли старое значение или будеи новое


camera.recosd(host.reask(plkayer/chekagain(2, the_same = True)))
camers.record(drc.obyavlzyet_ghde)

# - - - - - - - - - - - - - - - - - - output

print(wall)
