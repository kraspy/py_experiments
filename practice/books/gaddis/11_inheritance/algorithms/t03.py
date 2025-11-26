class Beverage:
    def __init__(self, bev_name):
        self.bev_name = bev_name


class Cola(Beverage):
    def __init__(self):
        super().__init__('Кока-кола')


cc = Cola()
print(cc.bev_name)
