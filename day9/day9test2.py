import math
class Point:
    def __init__(self, x, y, z=0):
        self.x = x
        self.y = y
        self.z = z
        print(f"创建了Point({self.x}, {self.y}, {self.z})")
    def __del__(self):
        print(f"销毁了Point({self.x}, {self.y}, {self.z})")
    def __add__(self, other):
        if isinstance(other, Vector):
            return Point(self.x + other.x, self.y + other.y, self.z + other.z)
        elif isinstance(other, Point):
            raise ValueError("不能将两个Point类相加")
        else:
            raise ValueError("错误")
    def __sub__(self, other):
        if isinstance(other, Vector):
            return Point(self.x - other.x, self.y - other.y, self.z - other.z)
        elif isinstance(other, Point):
            return Vector(self.x - other.x, self.y - other.y, self.z - other.z)
        else:
            raise ValueError("错误")
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z
    def __lt__(self, other):
        origin = Point(0, 0, 0)
        return self.distance(origin) < other.distance(origin)
    def distance(self, other):
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2 + (self.z - other.z) ** 2)
    def __str__(self):
        return f"Point({self.x}, {self.y}, {self.z})"

class Vector:
    def __init__(self, x, y, z=0):
        self.x = x
        self.y = y
        self.z = z
        print(f"创建了Vector({self.x}, {self.y}, {self.z})")
    def __del__(self):
        print(f"销毁了Vector({self.x}, {self.y}, {self.z})")
    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y, self.z + other.z)
        else:
            raise ValueError("错误")
    def __sub__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y, self.z - other.z)
        else:
            raise ValueError("错误")
    def __rotate1__(self, x):
        # 逆时针
        radians = math.radians(x)
        new_x = self.x * math.cos(radians) - self.y * math.sin(radians)
        new_y = self.x * math.sin(radians) + self.y * math.cos(radians)
        return Vector(new_x, new_y, self.z)
    def __rotate2__(self, x):
        # 顺时针
        radians = math.radians(x)
        new_x = self.x * math.cos(radians) + self.y * math.sin(radians)
        new_y = -self.x * math.sin(radians) + self.y * math.cos(radians)
        return Vector(new_x, new_y, self.z)
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z
    def __str__(self):
        return f"Vector({self.x}, {self.y}, {self.z})"
x = float(input("请输入 x 坐标："))
y = float(input("请输入 y 坐标："))
z = float(input("请输入 z 坐标（按回车跳过）: "))
point = Point(x, y, z)
x = float(input("请输入 x 坐标："))
y = float(input("请输入 y 坐标："))
z = float(input("请输入 z 坐标（按回车跳过）: "))
vector = Vector(x, y, z)
print(f"{point}/{vector}")