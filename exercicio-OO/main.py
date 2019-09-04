from OO01 import Person, Student
from OO02 import Contact, LegalPerson, PhysicalPerson

print("\n **** Instance of the physical person ****")

individual = PhysicalPerson("111111111", "256.698.547-88", "Mayara", "Rysia", "Rua do Sol", "Poço", 5700000, "Maceió", "Alagoas")

print("\n\t RG: ", individual.getRg())
print("\n\t CPF: ", individual.getCpf())
print("\n\t First Name: ", individual.getFirstName())
print("\n\t Last Name: ", individual.getLastName())
print("\n\t Adress: ", individual.getAdress())
print("\n\t Neighborhood: ", individual.getNeighborhood())
print("\n\t Zip Code: ", individual.getZipCode())
print("\n\t City: ", individual.getCity())
print("\n\t State: ", individual.getState())

print("\n **** Instance of the individual ****")

person = Person("Maria", "Brasileira", "Rua do Brasil", "Poço", 5000000, "Recife", "Pernambuco")

print("\n\tFirst Name: ", person.getFirstName())
print("\n\tLast Name: ", person.getLastName())
print("\n\tAdress: ", person.getAdress())
print("\n\tNeighborhood: ", person.getNeighborhood())
print("\n\tZip Code: ", person.getZipCode())
print("\n\tCity: ", person.getCity())
print("\n\tState: ", person.getState())

print("\n **** Instance of the legal entity ****")

legalPerson = LegalPerson("74.925.359/0001-06", "SS", person.getFirstName(), person.getLastName(), person.getAdress(), person.getNeighborhood(), person.getZipCode(), person.getCity(), person.getState())

print("\n\tCNPJ: ", legalPerson.getCnpj())
print("\n\tType: ", legalPerson.getType())
print("\n\tName: ", legalPerson.getFirstName() + " "+ legalPerson.getLastName())
print("\n\tAdress: ", legalPerson.getAdress())
print("\n\tNeighborhood: ", legalPerson.getNeighborhood())
print("\n\tZip Code: ", legalPerson.getZipCode())
print("\n\tCity: ", legalPerson.getCity())
print("\n\tState: ", legalPerson.getState())

print("\n **** Instance of the Student ****")

student = Student(individual.getFirstName(), individual.getLastName(),
individual.getAdress(), individual.getNeighborhood(), individual.getZipCode(),individual.getCity(), individual.getState(), 2019)

print("\t ", student.getFirstName(), student.getLastName(), student.getGraduationYear())

print("\n **** Instance of the Contact ****")

contact = Contact("email@gmail.com", "8855-5566", "11")

print("\n\tEmail: ", contact.getEmail())
print("\n\tTelephone: ", contact.getTelephone())
print("\n\tDDD: ", contact.getDdd())
