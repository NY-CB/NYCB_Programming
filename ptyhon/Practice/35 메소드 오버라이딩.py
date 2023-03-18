# 메소드 오버라이딩
# 자식 클래스에서 정의한 메소드를 쓰고싶을 때

from turtle import speed


class Unit: 

    def __init__(self, name, hp, speed): 
        self.name = name 
        self.hp = hp 
        self.speed = speed

    def move(self, location):
        print("[지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동 중입니다. [속도 {2}]".format(self.name, location, self.speed))


class AttackUnit(Unit): 
    def __init__(self, name, hp, speed, damage):
        Unit.__init__(self, name, hp, speed)      
        self.damage = damage 

    def attack(self, location): 
        print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]".format(self.name, location, self.damage))

    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))

# 다중 상속.
# 드랍쉽을 만든다면.

class Flyable:
    def __init__ (self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]".format(name, location, self.flying_speed))
        # 메소드 오버라이딩함.


# 공중공격유닛클래스
class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage) # 0은 지상 스피드를 의미.
        Flyable.__init__(self, flying_speed)

    def move(self, location):
        print("[공중 유닛 이동]")
        self.fly(self.name, location)


# 벌쳐

vulture = AttackUnit("벌쳐", 80, 10, 20)

# 배틀크루져

battlecruiser = FlyableAttackUnit("배틀크루져", 500, 25, 3)

vulture.move("11시")
battlecruiser.move("9시")

# 여기서 생기는 문제. 벌처는 무브 함수, 배틀은 플라이 함수를 써야함. 둘 다 움직이는 건데
# 매번 적기에는 존나 귀찮음.
# 그래서 메소드 오버라이딩을 씀.
# 걍 무브를 쓰고 싶을 때

