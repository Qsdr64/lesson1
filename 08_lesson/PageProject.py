import requests
class Yougiletest:

    def __init__(self, url)-> None:
        self.url = url

    def autauthorization(self, login, password, name):
        User =  {
            "login": login,
            "password": password,
            "name": name
            }
        req = requests.post(self.url + 'auth/companies', json = User)
        return req.json()
    
    def token (self, titel)