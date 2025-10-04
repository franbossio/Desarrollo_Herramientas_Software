from antlr4 import TerminalNode
from antlr4 import ErrorNode
from compiladorParser import compiladorParser
from compiladorListener import compiladorListener
from Tabla_Simbolos import TS, Variable


class Escucha(compiladorListener):

    def enterPrograma(self, ctx:compiladorParser.ProgramaContext):
        ts = TS.getTablaSimbolo()
        ts.addContexto()  # contexto global
        print("Comienza el parsing")

    def exitPrograma(self, ctx:compiladorParser.ProgramaContext):
        print("Fin del parsing")

    def exitDeclaracion(self, ctx:compiladorParser.DeclaracionContext):
        tipo = ctx.tipo().getText()

        # el primer identificador SIEMPRE está
        ids = [ctx.ID().getText()]

        # ahora recolectamos los que estén en listavar (si existe)
        def recolectar_listavar(lv, acumulador):
            if lv is not None and lv.ID() is not None:
                acumulador.append(lv.ID().getText())
                # llamada recursiva para seguir la cadena de comas
                recolectar_listavar(lv.listavar(), acumulador)

        recolectar_listavar(ctx.listavar(), ids)

        ts = TS.getTablaSimbolo()

        for nombre in ids:
            if ts.buscarSimbolo(nombre):
                print(f"Error: Variable '{nombre}' ya declarada")
            else:
                var = Variable(nombre, tipo)
                ts.addSimbolo(var)
                print(f"Se agregó la variable '{nombre}' de tipo '{tipo}' a la tabla de símbolos")
                
    def exitAsignacion(self, ctx:compiladorParser.AsignacionContext):
        nombre = ctx.ID().getText()  # el identificador al que se asigna
        valor = ctx.opal().getText() # el valor o expresión (opal es tu regla)

        ts = TS.getTablaSimbolo()
        simbolo = ts.buscarSimbolo(nombre)

        if simbolo is None:
            print(f"Error: Variable '{nombre}' no declarada antes de usarla")
        else:
            simbolo.inicializado = True
            print(f"Se asignó el valor '{valor}' a la variable '{nombre}'")