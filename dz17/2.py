#первым пришёл — первым ушёл
# Задание:
# Реализовать класс Queue
# Определить атрибут inside, который будет хранить в себе имена людей в очереди.
# Переопределить метод __str__, чтобы преобразовать его к виду: Name1=>Name2=>...=>Name3
# Реализовать методы:
# add - который добавляет имя в очередь
# take_out убирает первого человека из списка
# Переопределить методы __add__ , __sub__, __iadd__, __isub__ чтобы они соответствовали методам add и take_out

# __add__(self, other) - сложение. x + y вызывает x.__add__(y).
# __sub__(self, other) - вычитание (x - y).
# __iadd__(self, other) - +=.
# __isub__(self, other) - -=.
class Queue():
    inside =[]
    def add(self, name):
        self.inside.append(name)

    def take_out(self):
        self.inside.pop(0)

    def __add__(self,name):
        self.inside.append(name)

    def __sub__(self):
        self.inside.pop(0)

    def __iadd__(self, name):
        self.add(name)
        return self

    def __isub__(self,name ):
        self.take_out()
        return self
    def __str__(self):
        return '=>'.join(self.inside)
q=Queue()
q.add('Name1')
q+'Name2'
q+='Name3'
print (q)
q.take_out()
q-='Name3'
q.__sub__()
print (q)