from my_functions import estimate_max_hr, build_person, build_experiment, eingabe_experiment, eingabe_person, eingabe_person_test , eingabe_experiment_test
from my_classes import Saveable, Person, Experiment 


if __name__ == "__main__":

    speichername = input("Bitte Dateinamen eingeben: ")     #name der Datei, in der die Daten gespeichert werden sollen
    experiment = Experiment(*eingabe_experiment())
    experiment.__dict__ 
    
    anzahl_testpersonen = 1


    abfrage_eingabe = int(input("Neue Person eingeben (1) oder beenden (0): "))
    while abfrage_eingabe == 1:
        person = Person(*eingabe_person())      # Hier wird eine neue Person erstellt
        experiment.__dict__["Person " + str(anzahl_testpersonen)] = person.build_person() # Hier wird die Person dem Experiment hinzugefügt, mit build_person() wird ein dict mit der max-hr erstellt

        anzahl_testpersonen += 1
        abfrage_eingabe = int(input("Weitere Person eingeben (1) oder beenden (0): "))
    
    
    # Speichere das Experiment
    experiment.save(speichername + ".json")
    person.save(speichername + "_personen.json")
    #print(person.estimate_max_hr)
    