#Access point: public,protected,private

class Person:
    name= 'sam'
    _age= 28
    __height= 188
#class Male (person):
#     def show(self):
#   print(self._age):

m=Male()
m.show
print(Person._age)

#print(Person.name)
#print(Person._age)
#print(person.__height)

class Male(Person):
    def show(self):
        print(self._height)

print(Person._Person__height)
