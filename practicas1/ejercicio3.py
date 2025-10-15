
class Person:
    def __init__(self, name,age):
        self.name = name
        self.age = age
    
    def work(self):
        return f'{self.name} esta trabajando duro'
    
persona1 = Person('Santiago', 30)
persona2 = Person('Gerardo', 35)

print(persona1.work())
print(persona2.work())