import json


class Person():
    def __init__(self, first_name, last_name, age, sex):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.sex = sex

    def save(self):
        data = self.__dict__
        with open('person.json', 'w') as file:
            json.dump(data, file)

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
    
    def build_person(self):
      dict = { "first_name" : self.first_name,
             "last_name" : self.last_name,
             "age" : self.age,
             "estimate_max_hr" : self.estimate_max_hr()}
      return dict


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

#if __name__ == "__main__":
    #person = Person("John", "Doe", 25,)