from my_functions import estimate_max_hr, build_person, build_experiment

if __name__ == "__main__":
  #Experiment eingeben und anlegen
  supervisor = input("Bitte Name des Versuchsleiters eingeben: ")
  subject = input("Bitte Thema des Experiments eingeben: ")
  date = input("Bitte Datum eingeben: ")
  experiment_name = input("Bitte Name des Experiments eingeben: ")

  dict_experiment = build_experiment(experiment_name, date, supervisor, subject)

  #Eingabe der Personendaten mit Funktion
  def eingabe_person():
      first_name = input("Bitte Vorname der Testperson eingeben: ")
      last_name = input("Bitte Nachname der Testperson eingeben: ")
      sex = input("Bitte 'male' oder 'female' als Geschlecht eingeben: ")
      age = int(input("Bitte Alter der Testperson eingeben: "))
      return first_name, last_name, sex, age

  first_name, last_name, sex, age = eingabe_person()
  dict_person = build_person(first_name, last_name, sex, age)
  #Erste Testpeson in Dicronary Experiment anlegen
  anzahl_testpersonen = 1
  dict_experiment["Person " + str(anzahl_testpersonen)] = dict_person

  #Schleife bis alle Testpersonen angelegt sind
  weitere_person = int(input("Weitere Person eingeben (1) oder beenden (0): "))
  while weitere_person == 1:
      first_name, last_name, sex, age = eingabe_person()
      dict_person = build_person(first_name, last_name, sex, age)
      anzahl_testpersonen += 1
      dict_experiment["Person " + str(anzahl_testpersonen)] = dict_person
      weitere_person = int(input("Weitere Person eingeben (1) oder beenden (0): "))

  print(dict_experiment)

#Konnentar hinzu