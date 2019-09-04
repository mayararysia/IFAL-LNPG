from OO01 import Person

class Contact:

  def __init__(self, email, telephone, ddd):
    self._email = email
    self._telephone = telephone
    self._ddd = ddd
  
  def getEmail(self):
    return self._email
  
  def getTelephone(self):
    return self._telephone
  
  def getDdd(self):
    return self._ddd 
  
  def setTelephone(self, tel):
    self._telephone = tel
  
  def setEmail(self, email):
    self._email = email
  
  def setDdd(self, ddd):
    self._ddd = ddd

class LegalPerson(Person):
  
  def __init__(self, cnpj, typee, fname, lname, address, neighborhood, zipCode, city, state):
    self._cnpj = cnpj
    self._typee = typee
    super().__init__(fname, lname, address, neighborhood, zipCode, city, state)    

  def getCnpj(self):
    return self._cnpj
  
  def getType(self):
    return self._typee
  
  def setCnpj(self, cnpj):
    self._cnpj = cnpj
    
  def setType(self, typee):
    self._typee = typee


class PhysicalPerson(Person):

  def __init__(self, rg,  cpf, fname, lname, address, neighborhood, zipCode, city, state):
    self._rg = rg
    self._cpf = cpf
    super().__init__(fname, lname, address, neighborhood, zipCode, city, state)    

  def getRg(self):
    return self._rg
  
  def getCpf(self):
    return self._cpf
  
  def setRg(self, rg):
    self._rg = rg
  
  def setCpf(self, cpf):
    self._cpf = cpf

class Company(LegalPerson, PhysicalPerson):
  pass