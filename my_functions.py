def estimate_max_hr(age_years : int , sex : str) -> int:
  """
  See https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4124545/  [Titel anhand dieser PMC-ID in Citavi-Projekt übernehmen]  for different formulas
  """
  if sex == "male":
    max_hr_bpm =  223 - 0.9 * age_years
  elif sex == "female":
    max_hr_bpm = 226 - 1.0 *  age_years
  else:
    # der input() öffnet ein Eingabefenster für den Nutzer und speichert die Eingabe
    max_hr_bpm  = input("Enter maximum heart rate:")
  return int(max_hr_bpm)

def build_person(first_name, last_name, sex, age) -> dict:
    """Returns a dictionary of information about a supervisor or subject."""
    dict = { "first_name" : first_name,
             "last_name" : last_name,
             "age" : age,
             "estimate_max_hr" : estimate_max_hr(age,sex)}
    return dict

def build_experiment(experiment_name, date, supervisor, subject) -> dict:
    """Returns a dictionary of information about an experiment."""
    dict = {"experiment_name" : experiment_name,
            "date" : date,
            "supervisor" :   supervisor,
            "subject" :   subject
            }
    return dict

def eingabe_person():
    first_name = input("Bitte Vorname der Testperson eingeben: ")
    last_name = input("Bitte Nachname der Testperson eingeben: ")
    sex = input("Bitte 'male' oder 'female' als Geschlecht eingeben: ")
    age = int(input("Bitte Alter der Testperson eingeben: "))
    return first_name, last_name, sex, age

def eingabe_experiment():
    supervisor = input("Bitte Name des Versuchsleiters eingeben: ")
    subject = input("Bitte Thema des Experiments eingeben: ")
    date = input("Bitte Datum eingeben: ")
    experiment_name = input("Bitte Name des Experiments eingeben: ")
    return experiment_name, date, supervisor, subject

'''
def eingabe_experiment_test():
  supervisor = "hermann" #input("Bitte Name des Versuchsleiters eingeben: ")
  subject = "laufen" #input("Bitte Thema des Experiments eingeben: ")
  date = 23.4 #input("Bitte Datum eingeben: ")
  experiment_name = "vo2max" #input("Bitte Name des Experiments eingeben: ")
  return supervisor, subject, date, experiment_name
    

# Eingabe der Personendaten mit Funktion
def eingabe_person_test():
    first_name = "1"# input("Bitte Vorname der Testperson eingeben: ")
    last_name = "2" #input("Bitte Nachname der Testperson eingeben: ")
    sex = "male" # input("Bitte 'male' oder 'female' als Geschlecht eingeben: ")
    age = 23 #int(input("Bitte Alter der Testperson eingeben: "))
    return first_name, last_name, sex, age
'''