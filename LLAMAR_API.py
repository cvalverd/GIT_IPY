import hashlib
import requests
import json

def main_api():
    public = '4d7a4470912fabe21d52b952bd35938d'
    private = 'a8e874c014790a1bf05747e8a4a7b2b000711afd'
    ts = '1'
    hash = hashlib.md5((ts + private + public).encode()).hexdigest()
    
    base = 'http://gateway.marvel.com/v1/public/'
    caracter = requests.get(base + 'characters',
                            params={'apikey': public, 'ts': ts, 'hash' : hash, 'nameStartsWith': 'd'}).json()
    print(caracter)
    
if __name__ == '__main__':
    main_api()
	
	