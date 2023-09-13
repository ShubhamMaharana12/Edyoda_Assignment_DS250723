# Challenge 1: Square Numbers and Return Their Sum.

#Program:-

class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def sqSum(self):
        return self.x**2 + self.y**2 + self.z**2

x = int(input("Enter the value of X: \n"))
y = int(input("Enter the value of Y: \n"))
z = int(input("Enter the value of Z: \n"))

point = Point(x, y, z)
result = point.sqSum()
print(result)  