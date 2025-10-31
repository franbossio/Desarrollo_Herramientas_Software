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
        print("\n--- ANALISIS SEMANTICO ---")

    def exitPrograma(self, ctx:compiladorParser.ProgramaContext):
        ts = TS.getTablaSimbolo()
        print("\n--- ADVERTENCIA ---")
        for contexto in ts.contextos:
            for nombre, simbolo in contexto.simbolos.items():
                if isinstance(simbolo, Variable) and not simbolo.getUsado():
                    print(f"La variable '{nombre}' fue declarada pero nunca usada")

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
        nombre = ctx.ID().getText()  
        valor = ctx.opal().getText() 

        ts = TS.getTablaSimbolo()
        simbolo = ts.buscarSimbolo(nombre)

        if simbolo is None:
            print(f"Error: Variable '{nombre}' no declarada")
            return

        tipo_destino = simbolo.getTipoDato()
        tipo_valor = self.inferirTipo(valor, ts)

        if tipo_valor is None:
            print(f"Error: No se puede determinar el tipo del valor '{valor}'")
        elif tipo_destino != tipo_valor:
            print(f"Error: Tipos incompatibles en asignación '{nombre} = {valor}' "
                  f"({tipo_destino} ← {tipo_valor})")
        else:
            simbolo.setInicializado(True)
            simbolo.setUsado(True)
            #print(f"Asignación correcta: '{nombre}' ({tipo_destino}) = '{valor}' ({tipo_valor})")
            
    def exitFactor(self, ctx: compiladorParser.FactorContext):
        """
        Si en la regla 'factor' aparece un ID, significa que estamos usando una variable
        (por ejemplo: a = x + 2 → x es un factor)
        """
        if ctx.ID():
            nombre = ctx.ID().getText()
            ts = TS.getTablaSimbolo()
            simbolo = ts.buscarSimbolo(nombre)

            if simbolo is not None:
                simbolo.setUsado(True)
            else:
                print(f"Error: el identificador '{nombre}' no fue declarado.")

    def inferirTipo(self, valor, ts):
        """
        Dado un valor textual (por ejemplo 'x', '3', '4.2',)
        intenta deducir su tipo: 'int', 'float',  o el tipo de una variable existente.
        """
        # Literal entero
        if valor.isdigit():
            return "int"

        # Literal float (por ejemplo 3.14)
        try:
            float(valor)
            if "." in valor:
                return "float"
        except ValueError:
            pass

        # Literal string (por ejemplo "hola" o 'hola')
        if (valor.startswith("'") and valor.endswith("'")):
            return "char"

        # Si es una variable, buscamos su tipo
        simbolo = ts.buscarSimbolo(valor)
        if simbolo:
            return simbolo.getTipoDato()

        # Si no se puede determinar
        return None
