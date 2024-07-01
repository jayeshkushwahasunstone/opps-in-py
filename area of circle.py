class circle:
    def __init__(self,radius):
        self.radius=radius

    @property
    def area(self):
        return str((2*3.14*self.radius**2))
    @property
    def perimeter(self):
        return str((2*3.14*self.radius))

c1=circle(21)
print(c1.perimeter)
print(c1.area)
        
