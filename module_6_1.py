class Animal:
    alive = True
    fed = False

    def __init__(self, name):
        self.name = name
        self.food = None

    def __repr__(self):
        return self.name


class Mammal(Animal):
    def eat(self, food):
        self.food = food
        if food.edible is True:
            print(f'{self.name} съел {food.name}')
            self.fed = True
        elif food.edible is False:
            print(f'{self.name} не стал есть {food.name}')
            self.alive = False


class Predator(Animal):
    def eat(self, food):
        self.food = food
        if food.edible is True:
            print(f'{self.name} съел {food.name}')
            self.fed = True
        elif food.edible is False:
            print(f'{self.name} не стал есть {food.name}')
            self.alive = False


class Plant:
    edible = False

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name


class Flower(Plant):
    pass


class Fruit(Plant):
    edible = True


if __name__ == '__main__':
    a1 = Predator('Волк с Уолл-Стрит')
    a2 = Mammal('Хатико')
    p1 = Flower('Цветик семицветик')
    p2 = Fruit('Заводной апельсин')

    print(a1.name)
    print(p1.name)

    print(a1.alive)
    print(a2.fed)
    a1.eat(p1)
    a2.eat(p2)
    print(a1.alive)
    print(a2.fed)

    # Что произошло: Хищник попытался съесть цветок и погиб, млекопитающее съело фрукт и насытилось.
