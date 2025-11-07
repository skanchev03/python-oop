from project.animals.animal import Mammal
from project.food import Vegetable
from project.food import Fruit
from project.food import Meat
from project.food import Seed


class Mouse(Mammal):
    WEIGHT_PER_PIECE = 0.10

    def make_sound(self):
        return "Squeak"

    def feed(self, food):
        if isinstance(food, Vegetable) or isinstance(food, Fruit):
            self.weight += self.WEIGHT_PER_PIECE * food.quantity
            self.food_eaten += food.quantity
        else:
            return f"Mouse does not eat {food.__class__.__name__}!"


class Dog(Mammal):
    WEIGHT_PER_PIECE = 0.40

    def make_sound(self):
        return "Woof!"

    def feed(self, food):
        if isinstance(food, Meat):
            self.weight += self.WEIGHT_PER_PIECE * food.quantity
            self.food_eaten += food.quantity
        else:
            return f"Dog does not eat {food.__class__.__name__}!"


class Cat(Mammal):
    WEIGHT_PER_PIECE = 0.30

    def make_sound(self):
        return "Meow"

    def feed(self, food):
        if isinstance(food, Vegetable) or isinstance(food, Meat):
            self.weight += self.WEIGHT_PER_PIECE * food.quantity
            self.food_eaten += food.quantity
        else:
            return f"Cat does not eat {food.__class__.__name__}!"


class Tiger(Mammal):
    WEIGHT_PER_PIECE = 1.00

    def make_sound(self):
        return "ROAR!!!"

    def feed(self, food):
        if isinstance(food, Meat):
            self.weight += self.WEIGHT_PER_PIECE * food.quantity
            self.food_eaten += food.quantity
        else:
            return f"Tiger does not eat {food.__class__.__name__}!"
