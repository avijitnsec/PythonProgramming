class Shape:
    def shape(self):
        raise NotImplementedError("Not implemented for this type.")


class Square(Shape):
    def shape(self):
        print("Square.. ")


class Circle(Shape):
    def shape(self):
        print("Circle.. ")


class ShapeFactory:
    
    @staticmethod
    def getshape(self, type1):
        if type1 is None:
            print('No shape mentioned.. ')

        if type1 is "Circle":
            return Circle()

        if type1 is "Square":
            return Square()


if __name__ == '__main__':
    factory = ShapeFactory()
    factory.getshape("Circle").shape()
    factory.getshape("Square").shape()
