# Задание: Разработать консольную игру "Битва героев" на Python с использованием классов и разработать план проекта по этапам/или создать kanban доску для работы над данным проектом
# Общее описание:
# Создайте простую текстовую боевую игру, где игрок и компьютер управляют героями с различными характеристиками. Игра состоит из раундов, в каждом раунде игроки по очереди наносят урон друг другу, пока у одного из героев не закончится здоровье.
# Требования:
# Используйте ООП (Объектно-Ориентированное Программирование) для создания классов героев.
# Игра должна быть реализована как консольное приложение.
# Классы:
# Класс Hero:
# Атрибуты:
# Имя (name)
# Здоровье (health), начальное значение 100
# Сила удара (attack_power), начальное значение 20
# Методы:
# attack(other): атакует другого героя (other), отнимая здоровье в размере своей силы удара
# is_alive(): возвращает True, если здоровье героя больше 0, иначе False
# Класс Game:
# Атрибуты:
# Игрок (player), экземпляр класса Hero
# Компьютер (computer), экземпляр класса Hero
# Методы:
# start(): начинает игру, чередует ходы игрока и компьютера, пока один из героев не умрет. Выводит информацию о каждом ходе (кто атаковал и сколько здоровья осталось у противника) и объявляет победителя.


class Hero():
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.attack_power = 20
        self.is_alive = True


    def attack_other(self):
        return self.attack_power


    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.is_alive = False
            return True
        return False

class Game():
    def __init__(self, player_name, computer_name):
        self.player = Hero(player_name)
        self.computer = Hero(computer_name)


    def start(self):
        while True:
            print(f"\n{self.player.name}: {self.player.health} HP, {self.computer.name}: {self.computer.health} HP")
            self.player_turn()
            if not self.computer.is_alive:
                print(f"\n{self.player.name} wins!")
                return
            self.computer_turn()
            if not self.player.is_alive:
                print(f"\n{self.computer.name} wins!")
                return

            print("\n--- Round Over ---")



    def player_turn(self):
        damage = self.player.attack_other()
        if self.computer.take_damage(damage):
            print(f"{self.computer.name} is dead!")
        else:
            print(f"{self.player.name} attacks {self.computer.name} for {damage} HP!")
        self.player.attack_power += 5
        print(f"{self.player.name}'s attack power increases to {self.player.attack_power}")


    def computer_turn(self):
        damage = self.computer.attack_other()
        if self.player.take_damage(damage):
            print(f"{self.player.name} is dead!")
        else:
            print(f"{self.computer.name} attacks {self.player.name} for {damage} HP!")


player1 = Hero('Rog')
player2 = Hero('Computer')
game = Game(player1.name, player2.name)
game.start()




