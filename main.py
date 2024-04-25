from abc import ABC, abstractmethod

# Шаг 1: Создание абстрактного класса Weapon
class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass

# Шаг 2: Реализация конкретных типов оружия
class Sword(Weapon):
    def attack(self):
        return "Удар мечом"

class Bow(Weapon):
    def attack(self):
        return "Выстрел из лука"

class Spear(Weapon):
    def attack(self):
        return "Удар копьем"

# Шаг 3: Модификация класса Fighter
class Fighter:
    def __init__(self, name, weapon):
        self.name = name
        self.weapon = weapon

    def changeWeapon(self, new_weapon):
        self.weapon = new_weapon

    def fight(self, monster):
        print(f"{self.name} выбирает {type(self.weapon).__name__}.")
        print(f"{self.name} наносит {self.weapon.attack()}.")
        print(f"Монстр побежден!")

# Шаг 4: Реализация боя
fighter1 = Fighter("Герой", Sword())
fighter2 = Fighter("Злобный монстр", Bow())

fighter1.fight(fighter2)
fighter1.changeWeapon(Bow())
fighter1.fight(fighter2)
fighter1.changeWeapon(Spear())
fighter1.fight(fighter2)