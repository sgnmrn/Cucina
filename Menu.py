__author__ = 'marino'

import json

class Piatto:

    def __init__(self,nome, costo):
        self.nome = nome
        self.costo = costo

def crea(nomeFile) :
    lis =[]
    lis.append(Piatto("ravioli",10))
    lis.append(Piatto("rigatoni",8))
    lis.append(Piatto("linguine",9))
    lis.append(Piatto("risotto",11))
    ret = json.dumps(lis,default=(lambda v: list(v) if isinstance(v, set) else v.__dict__),indent =4)
    fi=open(nomeFile,'w')
    fi.write(ret)

def getMenu() :
    lis =[]
    lis.append(Piatto("ravioli",10))
    lis.append(Piatto("rigatoni",8))
    lis.append(Piatto("linguine",9))
    lis.append(Piatto("risotto",11))
    ret = json.dumps(lis,default=(lambda v: list(v) if isinstance(v, set) else v.__dict__),indent =4)
    return ret