class Area:

    instances = dict()
    
    def __new__(cls, lenght, width):
        return cls.instances.setdefault((lenght, width), super().__new__(cls))


class Building:

    def __init__(self, area: Area):
        
        self.cost: int = 0
        self.area: Area = area