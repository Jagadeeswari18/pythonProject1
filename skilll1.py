import math
class area:
    def init(self, l):
        self.l = l
    def areacir(self):
        res = 3.14 * l * l
        print("area of circle:" + " ")
        print(res)

    def perimeter_of_circle(self):
        per = (2 * 3.14 * l)
        print(per)


class rect(area):
    def init(self, l, b):
        area.init(self, l)
        self.b = b

    def arearec(self):
        res = l * b
        print(res)

    def perimeter_of_rectangle(self):
        p = 2 * (l + b)
        print(p)


class tri(rect):
    def init(self, l, b, h):
        rect.init(self, l, b)
        self.h = h

    def areatri(self):
        s = (l + b + h) / 2
        res = math.sqrt(s * (s - l) * (s - b) * (s - h))
        print(res)
