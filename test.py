import requests

class Person():
    def __init__(self, first_name):
        self.first_name = first_name
    
    def put(self, server_url):
        data = {'first_name': self.first_name}
        response = requests.put(server_url, json=data)
        if response.status_code == 201:
            print("Person erfolgreich auf dem Webserver erstellt.")
        else:
            print("Fehler beim Erstellen der Person auf dem Webserver.")

