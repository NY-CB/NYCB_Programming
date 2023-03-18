# 스타크래프트를 예

#마린

name = "marine" # 유닛의 이름
hp = 40 # 체력
damage = 5 # 공격력

print("{} 유닛이 생성되었습니다.".format(name))
print("체력 {0}, 공격력 {1}\n".format(hp,damage))

# 탱크 

tank_name = "tank"
tank_hp = 150
tank_damage = 35
print("{} 유닛이 생성되었습니다.".format(tank_name))
print("체력 {0}, 공격력 {1}\n".format(tank_hp,tank_damage))

tank2_name = "tank"
tank2_hp = 150
tank2_damage = 35
print("{} 유닛이 생성되었습니다.".format(tank2_name))
print("체력 {0}, 공격력 {1}\n".format(tank2_hp,tank2_damage))

def attack(name, location, damage):
    print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]".format(name, location, damage))

attack(name, "1시", damage)
attack(tank_name, "1시", tank_damage)
attack(tank2_name, "1시", tank2_damage)

# 게임에서나 아무튼 어떤 상황에서 같은 개체가 생겨날 때마다 1,2,3이라는 수를 붙여주기에는 너무 힘드니까 class를 사용한다.
# 붕어빵 틀


class Unit: 
    def __init__(self, name, hp, damage): # __init__ 생성자 -> 객채가 만들어질 때 자동으로 호출되는 것.
        #class로부터 만들어지는 것. init 함수에 정의된 갯수만큼 만들어야 결과로 나옴.
        self.name = name #멤버 변수
        self.hp = hp #멤버변수
        self.damage = damage #멤버변수
        print("{0} 유닛이 생성 되었습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))

# 이름 = 클래스 명
# marine1 = Unit("marine", 40, 5)
# marine2 = Unit("marine", 40, 5)
# tank = Unit("tank", 150, 35)

#레이스
wraith1 = Unit("레이스", 80, 5)
print("유닛이름: {0}, 공격력: {1}".format(wraith1.name, wraith1.damage))

#다크아칸이 마인드 컨트롤 씀
wraith2 = Unit("빼앗은 레이스", 80, 5)
wraith2.clocking = True

# 어떤 객체에 추가로 변수를 외부에서 만들어서 쓸 수 있음.

if wraith2.clocking == True:
    print("{0} 는 현재 클로킹 상태입니다.".format(wraith2.name))

# 레이스1에는 클로킹이 없어서 레이스을 바로 위에 함수에 넣고 돌리면 clocking을 추가하고 실행하라는 것이 나옴
# 이 것은 새로운 함수를 추가해야하는 것을 의미하는데, 외부에서 함수를 추가(확장)할 수도 있다는 것을 의미함


# 공격 유닛 / 메소드

class AttackUnit:
    def __init__(self, name, hp, damage): # __init__ 생성자 -> 객채가 만들어질 때 자동으로 호출되는 것.
        #class로부터 만들어지는 것. init 함수에 정의된 갯수만큼 만들어야 결과로 나옴.
        self.name = name #멤버 변수
        self.hp = hp #멤버변수
        self.damage = damage #멤버변수
        
    def attack(self, location): # ""메소드 앞에서는 항상 self를 적어줌.""
        print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]".format(self.name, location, self.damage))

    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))
        
firebat1 = AttackUnit("파이어뱃", 50, 16)
firebat1.attack("5시")

#공격 2번 받음.

firebat1.damaged(25)
firebat1.damaged(25)


#상속.

# Unit이 있고, Attack 유닛이 있음.
# 메딕처럼 힐 유닛, 공격이 없는 유닛 만들기

class Unit: 
    def __init__(self, name, hp): # __init__ 생성자 -> 객채가 만들어질 때 자동으로 호출되는 것.
        #class로부터 만들어지는 것. init 함수에 정의된 갯수만큼 만들어야 결과로 나옴.
        self.name = name #멤버 변수
        self.hp = hp #멤버변수

class AttackUnit:
    def __init__(self, name, hp, damage): # __init__ 생성자 -> 객채가 만들어질 때 자동으로 호출되는 것.
        #class로부터 만들어지는 것. init 함수에 정의된 갯수만큼 만들어야 결과로 나옴.
        self.name = name #멤버 변수
        self.hp = hp #멤버변수
        self.damage = damage #멤버변수

# 여기서 보면 어떤 유닛이든 이름과 HP가 있음. 이럴 때 쓸 수 있는 것이 상속.
# 유닛의 정보를 상속받아 어택 유닛을 만들 수 있음.

class Unit: #부모 Class

    def __init__(self, name, hp): # __init__ 생성자 -> 객채가 만들어질 때 자동으로 호출되는 것.
        #class로부터 만들어지는 것. init 함수에 정의된 갯수만큼 만들어야 결과로 나옴.
        self.name = name #멤버 변수
        self.hp = hp #멤버변수


class AttackUnit(Unit): #자식 Class
    def __init__(self, name, hp, damage):
        Unit.__init__(self, name, hp)      
        self.damage = damage 

    def attack(self, location): # ""메소드 앞에서는 항상 self를 적어줌.""
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


# 공중공격유닛클래스
class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, damage)
        Flyable.__init__(self, flying_speed)

# 발키기 만들기

valkyrie = FlyableAttackUnit("발키리", 200, 6, 5)
valkyrie.fly(valkyrie.name, "3시")

# 메소드 오버라이딩

# 자식 클래스에서 정의한 메소드를 쓰고싶을 때

