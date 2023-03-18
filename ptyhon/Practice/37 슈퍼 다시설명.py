class Unit:
    def __init__(self):
        print("Unit 생성자")

class Flyable:
    def __init__(self):
        print("Flyable 생성자")

class FlyableUnit(Flyable, Unit):
    def __init__(self):
        super().__init__()
        Unit.__init__(self)
        Flyable.__init__(self)


# 드랍쉽
dropship = FlyableUnit()

# super를 사용해서 상속을 받을 때는 괄호 안에 상속받을 첫번째 클래스에 대해서만 상수가 호출이 된다.
# 다중 상속이 필요할 때는 