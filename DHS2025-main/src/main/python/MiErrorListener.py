from antlr4.error.ErrorListener import ErrorListener

class MiErrorListener(ErrorListener):
    def __init__(self):
        super(MiErrorListener, self).__init__()
        self.errores = []

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        mensaje = f"Error sintáctico en línea {line}, columna {column}: {msg}"

        texto_error = offendingSymbol.text if offendingSymbol else ""

        # --- Falta punto y coma
        if "missing ';'" in msg or "expecting ';'" in msg:
            mensaje = f"Errro: Falta un punto y coma ';' al final de la instrucción (línea {line})"

        # --- ANTLR no detecta el ';', pero el input termina con ID o tipo
        elif "no viable alternative" in msg and texto_error in ["int", "float", "double", "char", "ID"]:
            mensaje = f"Error: Posible falta de punto y coma ';' al final de la declaración (línea {line})"

        # --- Falta paréntesis de cierre
        elif "missing ')'" in msg or "expecting ')'" in msg:
            mensaje = f"Error: Falta un paréntesis de cierre ')' (línea {line})"

        # --- Falta paréntesis de apertura
        elif "missing '('" in msg or "expecting '('" in msg:
            mensaje = f"Error: Falta un paréntesis de apertura '(' (línea {line})"

        # --- Error general de formato
        elif "no viable alternative" in msg or "extraneous input" in msg:
            mensaje = f"Error de formato en la declaración de variables o instrucción (línea {line})"

        # --- Símbolo inesperado
        elif "mismatched input" in msg:
            mensaje = f"Símbolo inesperado cerca de '{offendingSymbol.text}' (línea {line})"

        self.errores.append(mensaje)
        print(mensaje)
