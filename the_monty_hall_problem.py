import random

show_dialogs = True  # показывать диалоги между участниками в процессе игры

# ================================  classes

class Door:
    """ Дверь
    Имеет свой номер и спрятанный за ней приз"""

    def __init__(self, number):

        self.number = number        # просто номер двери: 1, 2 или 3
        self.prize = "Undefined"    # наименование приза: "Car" ..
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
        self.car_place = random.randint(1, 3) # car_place - целое, номер выигрышной двери
        # теперь поместим в стену за дверь с выбранным номером а/м, за другие - коз ).
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

    def announce_prize_door(self): # объявляет призовую дверь
        return self.car_place

    @staticmethod
    def do_your_choice(attemp_number):
        return attemp_number # номер попытки


class Player:
    """Игрок. Выбирает, какую дверь открыть"""
    def __init__(self):
        self.selected_door = None

    def choose_door(self,attempt, the_same_door = False):
        # главная (основная) последовательность
        main_seq = [1, 2, 3]
        # создаем (вспомогательное) множество 1-300 (для более распределенного рандома)
        seq = [x for x in range (main_seq[0],main_seq[-1]*100+1,1)]
        # при первом выборе выбираем любую вообще
        if attempt == 1:  # попытка 1
            qwer = random.choice(seq)
            asd = self.accuracy(qwer)
            self.selected_door = asd
            return self.selected_door
        # при втором выборе: зависит выбирать ли ту же самую дверь
        if attempt == 2:  # попытка 2
            # если ту же самую
            if the_same_door:
                return self.selected_door
            # если надо другую
            else:
                main_seq.remove(self.selected_door)  # ; print(seq)
                self.selected_door = self.accuracy(random.choice(seq))
                return self.selected_door
    @staticmethod
    def accuracy(got_num): # повышение точности выбора двери
        if got_num > 200:
            return 3
        elif got_num > 100:
            return 2
        else:
            return 1

class Camera:
    '''Камера. Беспристрастно фиксирует происходящее в студии. Может показать все разультаты'''
    def __init__(self):
        #self.first_choice = None # первый выбор игрока
        #self.second_choice = None # второй выбор игрока
        #self.prize_door = None # номер двери, за которой а/м
        self.tape = []  # пленка, все записывается в нее: [frame0, frame1, ..]
        self.frame = [] # один кадр с пленки: [первый_выбор, второй_выбор, призовая_дверь]

    def record(self,choice): # запишем 1й выбор, далее 2й, далее призовую дверь
        self.frame.append(choice)
        if len(self.frame)==3:
            self.tape.append(self.frame)
            self.frame = []

    def switch_on(self): # включение камеры, заправка чистой пленки
        self.tape = []
        self.frame = []

    def show(self):
        for frame in self.tape:
            print(frame)


# ------------------------------------ body

# создаем двери, присвоим им номера
d1 = Door(1)
d2 = Door(2)
d3 = Door(3)

# все двери находятся в одной стене, коей будет словарь
door_list = [d1, d2, d3]
wall = dict([(x.number, x) for x in door_list])

# создаем режиссера, ведущего, игрока и камеру
director = Director()
host = Host()
player = Player()
camera = Camera()

# включаем камеру
camera.switch_on()

#=========================================================================================
# ========================== сам игровой процесс - далее в  цикл его 
#=========================================================================================

for double in range(10):
    # режиссером выбирает номер выигрышной двери, запоминает его и помещает за двери А/м и двух коз
    director.place_prize(wall)

    # ведущий узнает от режиссера номер выигрышной двери и запоминет его
    # в конце он сообщит за какой дверью был авто.
    director.inform(host)

    # ведущий должен спросить у грока, что он выберет, и камера должна это зафиксировать
    camera.record(player.choose_door(host.do_your_choice(1))) # первый раз
    camera.record(player.choose_door(host.do_your_choice(2), the_same_door = True)) # второй раз
    camera.record(host.announce_prize_door())

# results
camera.show()
print(wall) # оно в каждой итерации разное - исправлять
