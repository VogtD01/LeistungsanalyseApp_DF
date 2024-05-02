import json
import requests


class Person():
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        #self.age = age
        #self.sex = sex


    def save(self):
        data = self.__dict__
        with open('person.json', 'w') as file:
            json.dump(data, file)


    def build_person(self):
        dict = { "first_name" : self.first_name,
                "last_name" : self.last_name}
        return dict
    
    def put(self,url):
        # Defines the data putted to the API
        data = {
            "name": self.first_name
        }
        data_json = json.dumps(data)
        response = requests.put(url, data=data_json)

        return(response.status_code)


class Experiment():
    def __init__(self, supervisor, subject, date, experiment_name):
        self.supervisor = supervisor
        self.subject = subject
        self.date = date
        self.experiment_name = experiment_name

    def save(self, filename):
        data = self.__dict__
        with open(filename, 'w') as file:
            json.dump(data, file)

class Subject(Person):
    def __init__(self, first_name, last_name, birth_date, age, sex, email):
        super().__init__(first_name, last_name)
        self.__birth_date = birth_date
        self.age = age
        self.sex = sex
        self.email = email


    def estimate_max_hr(self):  
        age = self.age
        sex = self.sex
        if sex == "male":
            max_hr_bpm = 223 - 0.9 * age
        elif sex == "female":
            max_hr_bpm = 226 - 1.0 * age
        else:
            max_hr_bpm = int(input("Enter maximum heart rate:"))
        return int(max_hr_bpm)
            
    def save(self, filename):
        data = self.__dict__
        with open(filename, 'w') as file:
            json.dump(data, file)

    def update_email(self, url):
        # Defines the data posted to the API
        data = {
            "name": self.first_name,
            "email": self.email
        }
        data_json = json.dumps(data)
        response = requests.post(url, data=data_json)

        return(response.status_code)

class Supervisor(Person):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)


#if __name__ == "__main__":
    #person = Person("John", "Doe", 25,)