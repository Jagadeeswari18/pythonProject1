import math
class Skill():
    def __init__(self, radius):
        self.radius = radius
    def calperimeter( self):
            return math.pi* self .radius*self.radius
    def calarea(self):
            return 2*math.pi*self.radius

circle = Skill(5)
print(circle.calperimeter())
print(circle.calarea())





