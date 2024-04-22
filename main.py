from my_functions import estimate_max_hr, build_person, build_experiment, eingabe_person, eingabe_experiment, eingabe_subject
from my_classes import Person, Experiment, Subject

if __name__ == "__main__":
    #Experiment eingeben und anlegen
    dateiname = input("Bitte Dateinamen eingeben: ")
    experiment = Experiment(*eingabe_experiment())
    experiment.save(dateiname)

    #Eingabe der Personendaten mit Funktion
    first_name, last_name = eingabe_person()
    birth_date, age, sex = eingabe_subject()
    subject = Subject(first_name, last_name, birth_date, age, sex)
    subject.save(dateiname)
    print(subject.estimate_max_hr())
    print(subject.__dict__)

    erneute_eingabe = int(input("Wollen Sie eine neue Person eingeben (1) oder beenden (0) ? : "))
    while erneute_eingabe == 1:
        subject = Subject(*eingabe_person(), *eingabe_subject)      # Hier wird eine neue Person erstellt
        experiment.__dict__["Person " + str(erneute_eingabe)] = subject.build_person() # Hier wird die Person dem Experiment hinzugefügt, mit build_person() wird ein dict mit der max-hr erstellt

        erneute_eingabe += 1
        erneute_eingabe = int(input("Weitere Person eingeben (1) oder beenden (0): "))
    
    
    # Speichere das Experiment
    experiment.save(dateiname + ".json")
    
    print(subject.estimate_max_hr)

