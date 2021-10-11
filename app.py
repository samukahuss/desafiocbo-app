from flask import Flask
from flask_restful import Resource, Api
import socket
from random import randint
from datetime import datetime

app = Flask(__name__)
api = Api(app)

class Sena(Resource):
    
    def get(self):
        return {"Retorno": [
                            {"Azure instance: " : socket.gethostname(),
                             "Datetime: ": str(datetime.now()),
                             "Jogo gerado ": str(self.jogo())
                            }
                           ]
               }

    def jogo(self):
        numeros=[]
        sena=[]
        
        for n in range(1,61):
            numeros.append(n)
            
        for i in range(6):
            sena.append(numeros.pop(randint(1, len(numeros)-1)))
            
        sena.sort()
        return sena
        

api.add_resource(Sena, '/')

if __name__=='__main__': 
    app.run(debug=True)
