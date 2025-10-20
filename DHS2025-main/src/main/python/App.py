import sys
from antlr4 import *
from compiladorLexer  import compiladorLexer
from compiladorParser import compiladorParser
from Escucha import Escucha
from Caminante import Caminante
from MiErrorListener import MiErrorListener

# En caso de no poder ejecutar el programa Python por
# problemas de version (error ATNdeserializer), se
# pueden generar los archivos a mano.
#
# Ir a la carpeta donde esta el archivo .g4 y ejecutar 
#     antlr4 -Dlanguage=Python3 -visitor compilador.g4 -o .

def main(argv):
    
    archivo = "input/simple.txt"
    if len(argv) > 1 :
        archivo = argv[1]
    input = FileStream(archivo)
    lexer = compiladorLexer(input)
    stream = CommonTokenStream(lexer)
    parser = compiladorParser(stream)
    
     #-----------------------------------------
    miError = MiErrorListener()
    parser.addErrorListener(miError)
     #-----------------------------------------
    print("\n--- ERRORES SEMANTICOS DETECTADOS ---")
    escucha = Escucha()
    parser.addParseListener(escucha)
    tree = parser.programa()
    #visitante = Caminante()
    #visitante.visitPrograma(tree)
    #-----------------------------------------
    errores = miError.getErrores()
    if errores:
        print("\n--- ERRORES SINTÁCTICOS DETECTADOS ---")
        for e in errores:
            print(e)
     #-----------------------------------------
    print(escucha)
    
    # print(tree.toStringTree(recog=parser))

if __name__ == '__main__':
    main(sys.argv)