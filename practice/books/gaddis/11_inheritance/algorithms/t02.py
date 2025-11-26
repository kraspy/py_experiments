class Plant:
    def __init__(self, plant_type):
        self._plant_type = plant_type

    def message(self):
        print('Я - растение.')


class Tree(Plant):
    def __init__(self):
        super().__init__('дерево')

    def message(self):
        print('Я - дерево.')


p = Plant('саженец')
t = Tree()
p.message()
t.message()
