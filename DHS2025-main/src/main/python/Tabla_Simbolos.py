from abc import ABC, abstractmethod


class ID(ABC):
    def __init__(self, nombre, tipoDato):
        self.nombre = nombre
        self.tipoDato = tipoDato
        self.inicializado = False
        self.usado = False

    # Métodos getters
    def getNombre(self):
        return self.nombre

    def getTipoDato(self):
        return self.tipoDato

    def getInicializado(self):
        return self.inicializado

    def getUsado(self):
        return self.usado

    # Métodos setters
    def setInicializado(self, valor=True):
        self.inicializado = valor

    def setUsado(self, valor=True):
        self.usado = valor



class Variable(ID):
    def __init__(self, nombre, tipoDato):
        super().__init__(nombre, tipoDato)


class Funcion(ID):
    def __init__(self, nombre, tipoDato, args=None):
        super().__init__(nombre, tipoDato)
        self.args = args if args else []

    def getListaArgs(self):
        return self.args


class Contexto:
    def __init__(self):
        # Diccionario {nombre: ID}
        self.simbolos = {}

    def addSimbolo(self, id_obj):
        self.simbolos[id_obj.getNombre()] = id_obj

    def buscarSimbolo(self, nombre):
        return self.simbolos.get(nombre, None)


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
        if self.contextos:
            self.contextos.pop()

    def addSimbolo(self, simbolo):
        if self.contextos:
            self.contextos[-1].addSimbolo(simbolo)

    def buscarSimbolo(self, nombre):
        # Busca desde el contexto más interno al más externo
        for contexto in reversed(self.contextos):
            s = contexto.buscarSimbolo(nombre)
            if s:
                return s
        return None

    def buscarSimboloContexto(self, nombre):
        # Busca solo en el contexto actual
        if self.contextos:
            return self.contextos[-1].buscarSimbolo(nombre)
        return None