# 건물을 만들겠다
# 서플라이를 만들겠다.

import unittest


class Unit: 

    def __init__(self, name, hp, speed): 
        self.name = name 
        self.hp = hp 
        self.speed = speed

    def move(self, location):
        print("[지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동 중입니다. [속도 {2}]".format(self.name, location, self.speed))

class BuildingUnit(Unit): # 상속받고
    def __init__(self, name, hp, location):
        pass # 그냥 아무것도 안하고 일단 넘어간다는 의미. 함수를 완성하지 않았지만 걍 넘어가는.

supply_depot = BuildingUnit("서플라이 디폿", 500, "7시")

def game_start():
    print("[알림] 새로운 게임을 시작합니다.")

def game_over():
    pass

#-------------------------------------------------------------------
# 패스

class Unit: 

    def __init__(self, name, hp, speed): 
        self.name = name 
        self.hp = hp 
        self.speed = speed

    def move(self, location):
        print("[지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동 중입니다. [속도 {2}]".format(self.name, location, self.speed))

class BuildingUnit(Unit): # 상속받고
    def __init__(self, name, hp, location, location):
        Unit.__init__(self, name, hp, 0)
        super().__init__(name, hp, 0) # super를 쓸 때는 self를 쓰지 않지만 super 뒤에는 ()를 붙인다.
        self.location = location

Unit unit 
unit.

