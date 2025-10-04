# Tabla de símbolos singleton
class TS:
    _instance = None

    def __init__(self):
        self.contextos = []

    @staticmethod
    def getTablaSimbolo():
        if TS._instance is None:
            TS._instance = TS()
        return TS._instance

    def addContexto(self):
        self.contextos.append(Contexto())

    def delContexto(self):
        self.contextos.pop()

    def addSimbolo(self, simbolo):
        if self.contextos:
            self.contextos[-1].addSimbolo(simbolo)

    def buscarSimbolo(self, nombre):
        for contexto in reversed(self.contextos):
            s = contexto.buscarSimbolo(nombre)
            if s:
                return s
        return None

class Contexto:
    def __init__(self):
        self.simbolos = {}

    def addSimbolo(self, id_obj):
        self.simbolos[id_obj.nombre] = id_obj

    def buscarSimbolo(self, nombre):
        return self.simbolos.get(nombre, None)

class Variable:
    def __init__(self, nombre, tipoDato):
        self.nombre = nombre
        self.tipoDato = tipoDato
        self.inicializado = False
        self.usado = False
