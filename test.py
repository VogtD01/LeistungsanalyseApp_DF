import my_classes
from datetime import datetime

if __name__ == "__main__":
    
    print("---LeistungsanalyseApp---")
    print("->Running test file")
    print("->Generating sample objects")

    supervisor = my_classes.Supervisor("Flo" , "Justli")
    subject = my_classes.Subject("Domi" , "Vögtli", "male", datetime(2001, 5, 5), "Domi.vogelwild@mail.com")
    experiment = my_classes.Experiment("Leistungstest", datetime.now().strftime("%Y/%m/%d, %H:%M:%S"), supervisor, subject)
    
    print(f"Estimated max hartrate of subject: {subject.estimate_max_hr()}")
    print("->Saving sample objects to file")
    #supervisor.save("data")
    #subject.save("data")
    experiment.save("data")
    print("Succesfully saved")
    print("->Uploading sample data to webserver...")
    url = "http://localhost:5000/"
    supervisor.put(url)
    subject.put(url)
    subject.update_email(url)
    print("Succesfully uploaded")