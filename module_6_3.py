class Horse:
    def __init__(self, x_distance=0, sound='Frrr'):
        self.x_distance = x_distance
        self.sound = sound

    def run(self, dx):
        self.x_distance = dx


class Eagle:
    def __init__(self, y_distance=0, sound='I train, eat, sleep, and repeat'):
        self.y_distance = y_distance
        self.sound = sound

    def fly(self, dy):
        self.y_distance = dy


class Pegasus(Horse, Eagle):
    def __init__(self):
        self.x_distance = int()
        self.y_distance = int()
        super().__init__()

    def move(self, dx, dy):
        self.x_distance = dx
        self.y_distance = dy
        super().run(dx)
        super().fly(dy)

    pos = (0, 0)  # Текущая позиция

    def get_pos(self):
        x = self.x_distance
        y = self.y_distance
        move = (x, y)  # координаты движения
        self.pos = self.pos[0] + move[0], self.pos[1] + move[1]
        return self.pos

    def voice(self):
        Eagle.__init__(self)
        print(self.sound)


p1 = Pegasus()

print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())

p1.voice()
