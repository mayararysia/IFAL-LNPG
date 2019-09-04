class Person:

  def __init__(self, fname, lname, address, neighborhood, zipCode, city, state):
    self._firstname = fname
    self._lastname = lname
    self._address = address
    self._neighborhood = neighborhood
    self._zipCode = zipCode
    self._city = city
    self._state = state
  
  def getFirstName(self):
    return self._firstname

  def getLastName(self):
    return self._lastname
  
  def getAdress(self):
    return self._address
  
  def getNeighborhood(self):
    return self._neighborhood
  
  def getZipCode(self):
    return self._zipCode
  
  def getCity(self):
    return self._city
  
  def getState(self):
    return self._state

  def setFirstName(self, fname):
    self._firstname = fname

  def setLastName(self, lname):
    self._lastname = lname
  
  def setAdress(self, address):
    self._address = address
  
  def setNeighborhood(self, neighborhood):
    self._neighborhood = neighborhood
  
  def setZipCode(self, zipCode):
    self._zipCode = zipCode
  
  def setCity(self, city):
    self._city = city
  
  def setState(self, state):
    self._state = state

#subclass:
class Student(Person):
  def __init__(self, fname, lname, address, neighborhood, zipCode, city, state, year):
	  Person.__init__(self, fname, lname, address, neighborhood, zipCode, city, state)
	  self._graduationYear = year

  def getGraduationYear(self):
      return self._graduationYear

  def setGraduationYear(self, year):
      self._graduationYear = year

  def welcome(self):
    print("Welcome ", self.firstname, self.lastname, "to the class of", self.graduationyear)

  
  
 