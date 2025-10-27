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
STRING : 'string';
FLOAT: 'float';
CHAR: 'char';
IF :    'if' ;
ELSE :  'else' ;
FOR :   'for' ;
WHILE : 'while' ;

ID : (LETRA | '_')(LETRA | DIGITO | '_')* ;

WS : [ \n\r\t] -> skip ;
OTRO : . ;


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
          | VOID ID PA tipo ID listaDeclaracion PC instruccion; 

 
listaDeclaracion: COMA tipo ID listaDeclaracion
               | 
               ;

llamada :  ID PA opal listaLlamada PC PYC
          | tipo ID ASIG ID PA opal listaLlamada PC PYC
          | ID ASIG ID PA opal listaLlamada PC PYC;

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
     | FLOAT
     | CHAR
     ;


asignacion : ID ASIG opal PYC ;

opal : expresion op ;


op : opComp expresion op
     |
     ;

opComp : IGUAL | DISTINTO | MENOR | MAYOR | MENORIGUAL | MAYORIGUAL |AND |OR|NOT;


expresion : term e ;


e : SUMA term e
  | RESTA term e
  |
  ;


term : factor t ;

t : MULT factor t
  | DIV factor t
  | MOD factor t
  |
  ;


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