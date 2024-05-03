import json
import requests

class Person ():

  def __init__(self, first_name, last_name):
    self.first_name = first_name
    self.last_name = last_name
    

  def save(self, filename):
        
        with open(filename, 'w') as file:
            json.dump(self.__dict__, file)

  def put(self, server_url):
        # Nur der Vorname wird für die Erstellung der Person auf dem Webserver verwendet
        data = {'first_name': self.first_name}
        response = requests.put(server_url, json=data)
        if response.status_code == 201:
            print("Person erfolgreich auf dem Webserver erstellt.")
        else:
            print("Fehler beim Erstellen der Person auf dem Webserver.")


person1 = Person("Max", "Mustermann")
person1.put('http://127.0.0.1:5000/person/')

    

class Experiment ():

  def __init__(self, supervisor, subject, date, experiment_name):
    self.supervisor = supervisor
    self.subject = subject
    self.date = date
    self.experiment_name = experiment_name  

  def save(self, filename):
        
    with open(filename, 'w') as file:
        json.dump(self.__dict__, file)



############################################

#Subklassen

class Subject(Person):
    def __init__(self, first_name, last_name, sex, age, birth_date,email):
        # Die Funktion super() zeigt Python an, dass die __init__() aus der Elernklasse aufgerufen werden soll
        super().__init__(first_name, last_name)
        self.__birth_date = birth_date
        self.age = age
        self.sex = sex
        self.email = email

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
    
    def update_email(self, url):
        # Defines the data posted to the API
        data = {
            "name": self.first_name,
            "email": self.email
        }
        data_json = json.dumps(data)
        response = requests.post(url, data=data_json)


class Supervisor(Person):
     def __init__(self, first_name, last_name, id):
        # Die Funktion super() zeigt Python an, dass die __init__() aus der Elernklasse aufgerufen werden soll
        super().__init__(first_name, last_name)
        self.id = id
        



#p1 = Subject("Max", "Mustermann", "01.01.1990", 30, "male")
#p1.save("test.json")
#print(p1.estimate_max_hr())
#s1= Supervisor("Hans", "Müller", 123)
#print(s1.__dict__)