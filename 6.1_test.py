from my_functions import estimate_max_hr, build_person, build_experiment, eingabe_experiment, eingabe_person, eingabe_person_test , eingabe_experiment_test
from my_classes_old import Saveable, Person, Experiment 


if __name__ == "__main__":

    speichername = input("Bitte Dateinamen eingeben: ")
    experiment = Experiment(*eingabe_experiment_test())
    experiment.__dict__ 
    #person = Person(*eingabe_person_test())
    anzahl_testpersonen = 1


    abfrage_eingabe = int(input("Neue Person eingeben (1) oder beenden (0): "))
    while abfrage_eingabe == 1:
        person = Person(*eingabe_person_test())      # Hier wird eine neue Person erstellt
        experiment.__dict__["Person " + str(anzahl_testpersonen)] = person.__dict__ # Hier wird die Person dem Experiment hinzugefügt

        anzahl_testpersonen += 1
        abfrage_eingabe = int(input("Weitere Person eingeben (1) oder beenden (0): "))
    
    
    # Speichere das Experiment
    experiment.save(speichername + ".json")
    print(person.estimate_max_hr)
    