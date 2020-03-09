class PartyAnimal:
   x = 0

   def __init__(self): # Constructor
     print('I am constructed')

   def party(self) : # Method
     self.x = self.x + 1
     print('So far',self.x)

   def __del__(self): # Deconstructor
     print('I am destructed', self.x)

an = PartyAnimal()
print ("Type", type(an))
print ("Dir ", dir(an))
print ("Type", type(an.x))
print ("Type", type(an.party))

an.party()
an.party()
an = 42
print('an contains',an)


