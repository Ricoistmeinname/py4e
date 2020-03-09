class PartyAnimal:
   x = 0
   name = ''
   def __init__(self, nam): # Constructor - Code that runs when an object is created - grab the name parameter
     self.name = nam
     print(self.name,'constructed')

   def party(self) : # Method
     self.x = self.x + 1
     print(self.name,'party count',self.x)

