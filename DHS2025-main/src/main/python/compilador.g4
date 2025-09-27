grammar compilador;

fragment LETRA : [A-Za-z] ;
fragment DIGITO : [0-9] ;

PA : '(' ;
PC : ')' ;
LLA : '{' ;
LLC : '}' ;
PYC : ';' ;
ASIG : '=' ;
COMA : ',' ;
SUMA : '+' ;
RESTA : '-' ;
MULT : '*' ;
DIV : '/' ;
MOD : '%' ;
IGUAL : '==';
DISTINTO : '!=';
MENOR : '<';
MAYOR : '>';
MENORIGUAL : '<=';
MAYORIGUAL : '>=';
AND : '&&';
OR : '||';
NOT : '!';
CONTADOR : '++';
DESCONTAR : '--';
RETURN : 'return';
VOID : 'void';

NUMERO : DIGITO+ ;

INT : 'int' ;
DOUBLE : 'double' ;
IF :    'if' ;
ELSE :  'else' ;
FOR :   'for' ;
WHILE : 'while' ;

ID : (LETRA | '_')(LETRA | DIGITO | '_')* ;

WS : [ \n\r\t] -> skip ;
OTRO : . ;

// s : ID     {print("ID ->" + $ID.text + "<--") }         s
//   | NUMERO {print("NUMERO ->" + $NUMERO.text + "<--") } s
//   | OTRO   {print("Otro ->" + $OTRO.text + "<--") }     s
//   | EOF
//   ;

// s : PA s PC s
//   |
//   ;

programa : instrucciones EOF ;

instrucciones : instruccion instrucciones
              |
              ;

instruccion : asignacion
            | declaracion
            | iif
            | iwhile
            | bloque
            | ifor
            | funcion
            | llamada
            ;

funcion : tipo ID PA tipo ID listaDeclaracion PC PYC
          | tipo ID PA tipo ID listaDeclaracion PC LLA instrucciones RETURN ID PYC LLC
          | VOID ID PA tipo ID listaDeclaracion PC PYC
          | VOID ID PA tipo ID listaDeclaracion PC bloque; 

 
listaDeclaracion: COMA tipo ID listaDeclaracion
               | 
               ;

llamada :  ID PA opal listaLlamada PC PYC
          | tipo ID ASIG ID PA opal listaLlamada PC PYC;

listaLlamada : COMA opal listaLlamada
               |
               ;

bloque : LLA instrucciones LLC ;

iwhile : WHILE PA opal PC instruccion ;

iif : IF PA opal PC instruccion ielse ;

ielse : ELSE instruccion
      |
      ;

ifor : FOR PA  asignacion  opal PYC contador PC instruccion ;

declaracion : tipo ID inic listavar PYC ;

listavar : COMA ID inic listavar
         |
         ;

inic : ASIG opal
     |
     ;

tipo : INT
     | DOUBLE
     ;


asignacion : ID ASIG opal PYC ;

// Punto de entrada para expresiones lógicas o aritméticas
opal : expresion op ;


op : opComp expresion op
     |
     ;

opComp : IGUAL | DISTINTO | MENOR | MAYOR | MENORIGUAL | MAYORIGUAL |AND |OR|NOT;

// Expresión aritmética
expresion : exp ;

// Aritmética (+, -)
exp : term e ;

e : SUMA term e
  | RESTA term e
  |
  ;

// Aritmética (*, /, %)
term : factor t ;

t : MULT factor t
  | DIV factor t
  | MOD factor t
  |
  ;

// Factores: números, variables, paréntesis, negación lógica
factor : NUMERO
       | ID
       | PA opal PC
       | NOT factor    
       ;

contador : CONTADOR ID
          | DESCONTAR ID
          | ID CONTADOR
          | ID DESCONTAR
          |
          ;