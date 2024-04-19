import json

class Saveable:
    def save(self, filename):
        with open(filename, 'w') as file:
            json.dump(self.__dict__, file)


class Person ():

  def __init__(self, first_name, last_name, sex, age):
    self.first_name = first_name
    self.last_name = last_name
    self.sex = sex
    self.age = age

  def save(self, filename):
        data = {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "sex": self.sex,
            "age": self.age
        }
        with open(filename, 'w') as file:
            json.dump(data, file)


  def estimate_max_hr(self):
    if self.sex == "male":
          max_hr_bpm = 223 - 0.9 * self.age
    elif self.sex == "female":
            max_hr_bpm = 226 - 1.0 * self.age
    else:
            # Der input() öffnet ein Eingabefenster für den Nutzer und speichert die Eingabe
            max_hr_bpm = int(input("Enter maximum heart rate:"))
    return max_hr_bpm
  
  def build_person(self):
      """Returns a dictionary of information about a supervisor or subject."""
      dict = { "first_name" : self.first_name,
             "last_name" : self.last_name,
             "age" : self.age,
             "estimate_max_hr" : self.estimate_max_hr()}
      return dict
    

class Experiment (Saveable):

  def __init__(self, supervisor, subject, date, experiment_name):
    self.supervisor = supervisor
    self.subject = subject
    self.date = date
    self.experiment_name = experiment_name  


#p1 = Person("Max", "Mustermann", 1990)
#p4.save("personen.json")
#p4 = Person("Dominic", "Doe", "male", 1990)
#p3 = Person("flo", "just", "female", 26)
#p4.save("personen.json")
#p3.save("personen.json")
#print(p3.estimate_max_hr())
#print(p3.build_person())