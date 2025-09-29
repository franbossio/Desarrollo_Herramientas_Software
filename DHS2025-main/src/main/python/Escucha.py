from compiladorParser import compiladorParser
import compiladorListener

class Escucha (compiladorListener) : 
    def enterPrograma(self, ctx:compiladorParser.ProgramaContext):
        print('Comienza el parsing')
        
    def exitPrograma(self, ctx:compiladorParser.ProgramaContext):
        print('Termina el parsing')
        