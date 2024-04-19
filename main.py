from my_functions import estimate_max_hr, build_person, build_experiment, eingabe_person, eingabe_experiment
from my_classes import Person, Experiment

if __name__ == "__main__":
    #Experiment eingeben und anlegen
    dateiname = input("Bitte Dateinamen eingeben: ")
    experiment = Experiment(*eingabe_experiment())
    experiment.save()

    #Eingabe der Personendaten mit Funktion
    person = Person(*eingabe_person())
    person.save()
    print(person.estimate_max_hr())
    print(person.__dict__)

    erneute_eingabe = int(input("Wollen Sie eine neue Person eingeben (1) oder beenden (0) ? : "))
    while erneute_eingabe == 1:
        person = Person(*eingabe_person())      # Hier wird eine neue Person erstellt
        experiment.__dict__["Person " + str(erneute_eingabe)] = person.build_person() # Hier wird die Person dem Experiment hinzugefügt, mit build_person() wird ein dict mit der max-hr erstellt

        erneute_eingabe += 1
        erneute_eingabe = int(input("Weitere Person eingeben (1) oder beenden (0): "))
    
    
    # Speichere das Experiment
    experiment.save(dateiname + ".json")
    
    print(person.estimate_max_hr)
