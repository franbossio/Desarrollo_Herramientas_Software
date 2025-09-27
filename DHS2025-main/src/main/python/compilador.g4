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
opal : logica ;

// Operadores lógicos (|| tiene menor precedencia que &&)
logica : comparacion (OR comparacion)* ;

// Comparaciones (==, !=, <, >, <=, >=)
comparacion : expresion (opComp expresion)? ;

opComp : IGUAL | DISTINTO | MENOR | MAYOR | MENORIGUAL | MAYORIGUAL ;

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
       | NOT factor    // para !a o !(a < b)
       ;

contador : CONTADOR ID
          | DESCONTAR ID
          | ID CONTADOR
          | ID DESCONTAR
          |
          ;