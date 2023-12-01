class Tomato:
    maturation_stages = ['absent', 'flowering', 'green', 'red']
    def __init__(self, index):
        self.index = index
        self._state = Tomato.maturation_stages[0]
        
    def grow(self):
        if self._state != Tomato.maturation_stages[-1]:
            self._state =  Tomato.maturation_stages[ Tomato.maturation_stages.index(self._state) + 1]

    def is_ripe(self):
        return self._state == Tomato.maturation_stages[-1]

class TomatoBush:
    
    def __init__(self, number_tomatoes):
        self.number_tomatoes = number_tomatoes
        self.tomatoes = [Tomato(i) for i in range(number_tomatoes)]
        
    def grow_all(self):
        for tomato in self.tomatoes:
            tomato.grow()
    
    
    def all_are_ripe(self):
        for tomato in self.tomatoes:
            if not tomato.is_ripe:
                return False
        return True
    
    def give_away_all(self):
        self.tomatoes.clear()
        
class Gardener:
    
    def __init__(self, name, plant):
        self.name = name
        self._plant = plant
        
    def work(self):
        self._plant.grow_all()
        
    def harvest(self):
        if self._plant.all_are_ripe():
            self._plant.give_away_all()
        else:
            print('Не все плоды созрели')
        
    def knowledge_base(self):
        print('Справка:')
        if self._plant.all_are_ripe():
            print('Все плоды созрели')
        else:
            print('Не все плоды созрели')
        if len(self._plant.tomatoes) == 0:
            print('Все плоды собраны')
        else:
            print('Плоды еще не собраны')
            
            
            
# Тетсы:
# Тест 1
a = TomatoBush(5)
b = Gardener('John', a)
# Тест 2
b.work()
# Тест 3    
b.harvest()
for _ in range(3):
    b.work()
# Тест 4
b.harvest()   
# Тест 5
b.knowledge_base()