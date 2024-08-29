class AreaRect:

    def __init__(self, length, breath):
        self.length = length
        self.breath = breath

    def calculate_area(self):
        return self.length * self.breath

area1 = AreaRect(10, 66)
area2 = AreaRect(299, 733)

print(area1.calculate_area())
print(area2.calculate_area())