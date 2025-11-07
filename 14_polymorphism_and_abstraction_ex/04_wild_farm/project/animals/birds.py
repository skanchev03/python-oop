from project.animals.animal import Bird
from project.food import Vegetable
from project.food import Fruit
from project.food import Meat
from project.food import Seed


class Owl(Bird):
    WEIGHT_PER_PIECE = 0.25

    def make_sound(self):
        return "Hoot Hoot"

    def feed(self, food):
        if isinstance(food, Meat):
            self.weight += self.WEIGHT_PER_PIECE * food.quantity
            self.food_eaten += food.quantity
        else:
            return f"Owl does not eat {food.__class__.__name__}!"

class Hen(Bird):
    WEIGHT_PER_PIECE = 0.35

    def make_sound(self):
        return "Cluck"

    def feed(self, food):
        self.weight += self.WEIGHT_PER_PIECE * food.quantity
        self.food_eaten += food.quantity
