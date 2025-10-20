from compiladorVisitor import compiladorVisitor
from compiladorParser import compiladorParser

class Caminante (compiladorVisitor):
    instr=0
    def visitPrograma(self, ctx:compiladorParser.ProgramaContext):
        print('Programa procesado')
        return self.visitChildren(ctx)
    
    def visitInstruccion(self, ctx:compiladorParser.InstruccionContext):
        self.instr +=1
        print('Instruccion' + str(self.instr))
        print('\t' + ctx.getText())
        return self.visitChildren(ctx)
    
    def visitListaDeclaracion(self, ctx:compiladorParser.ListaDeclaracionContext):
        print('Declaracion' + str(self.instr))
        print('\t' + ctx.getText())
        return self.visitChildren(ctx)