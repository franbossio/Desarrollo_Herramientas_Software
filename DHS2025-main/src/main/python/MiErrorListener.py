from antlr4.error.ErrorListener import ErrorListener

class MiErrorListener(ErrorListener):
    def __init__(self):
        super(MiErrorListener, self).__init__()
        self.errores = []

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        mensaje = f"❌ Error sintáctico en línea {line}, columna {column}: {msg}"
      
        if "input" in msg:
            mensaje = f"❌ Falta un punto y coma ';' al final de la instrucción (línea {line})"

        elif "missing ')'" in msg:
            mensaje = f"❌ Falta un paréntesis de cierre ')' (línea {line})"

        elif "no viable alternative" in msg:
            mensaje = f"❌ Error de formato en la declaración o instrucción (línea {line})"


        self.errores.append(mensaje)

    def getErrores(self):
        return self.errores
