from antlr4.error.ErrorListener import ErrorListener

class MiErrorListener(ErrorListener):
    def __init__(self):
        super(MiErrorListener, self).__init__()
        self.errores = []

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        mensaje = f"\n--- ERROR SINTACTICO ---\nError en la línea {line}, columna {column}: {msg}\n------------------------------------------------------\n"

        # --- Falta punto y coma
        if "no viable alternative at input" in msg:
            mensaje = f"\n--- ERROR SINTACTICO ---\nPosible falta de un punto y coma ';' al final de la instrucción (línea {line})\n------------------------------------------------------\n"

        # --- Falta paréntesis de cierre
        elif "missing ')'" in msg or "expecting ')'" in msg:
            mensaje = f"\n--- ERROR SINTACTICO ---\nFalta un paréntesis de cierre ')' (línea {line})\n------------------------------------------------------\n"

        # --- Falta paréntesis de apertura
        elif "extraneous input ')' expecting ';'" in msg:
            mensaje = f"\n--- ERROR SINTACTICO ---\nFalta un paréntesis de apertura '(' (línea {line})\n------------------------------------------------------\n"

        # --- Formato incorrecto en lista de declaración de variables
        elif "missing ID" in msg:
            mensaje = f"\n--- ERROR SINTACTICO ---\nFormato incorrecto en lista de declaración de variables (línea {line})\n------------------------------------------------------\n"


        self.errores.append(mensaje)
        print(mensaje)
