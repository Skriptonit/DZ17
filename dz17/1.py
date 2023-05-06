# Задание: Создайте класс Batary, у которой будет определен атрибут capacity = [ ] (емкость),
# max_charge = 5 (максимальный заряд) по умолчанию, и методы:
# charge - заряжает батарею
# discharge - разряжает батарею.
# Переопределите метод __str__, чтобы при вызове экземпляра он представлялся в виде: [)))))] - максимально заряженная батарея.
class Batary():
    capacity=[]
    max_charge = 5
    def charge(self,charge):
        self.capacity.append(charge)
    def discharge(self):
        self.capacity.pop()
    def __str__(self):
        return "[" + "".join(self.capacity) + "]"

b=Batary()
i=0
while b.max_charge>i:
    b.charge(')')
    i+=1
print(b)
