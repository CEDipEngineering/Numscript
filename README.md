# Numscript
My own programming language, using only symbols and numbers. Meant to be programmed using only a numpad and a few extra symbols.

# EBNF

`

    BLOCK = '{' , { STATEMENT }, '}' ;

    STATEMENT = ( λ | ASSIGNMENT | PRINT | DECLARATION), ';';
                | (BLOCK | WHILE | IF);

    FACTOR = NUMBER | IDENTIFIER | (('+' | '-' | '!') , FACTOR) | '(' , RELEXPRESSION , ')' | SCANF;

    TERM = FACTOR, { ('*' | '/' | '&&'), FACTOR } ;

    EXPRESSION = TERM, { ('+' | '-' | '||'), TERM } ;

    RELEXPRESSION = EXPRESSION , {('<' | '>' | '==') , EXPRESSION } ;

    WHILE = '$_436_2', '(', RELEXPRESSION ,')', STATEMENT;

    IF = '$_436_0', '(', RELEXPRESSION ,')', STATEMENT, (('$_436_1', STATEMENT) | λ );

    ASSIGNMENT = IDENTIFIER, '=' , EXPRESSION ;

    PRINT = '$_436_3', '(' , EXPRESSION, ')' ;

    SCANF = '$_436_4', '(', ')' ;

    IDENTIFIER = $, DIGIT | '_', { DIGIT | '_' } ;

    NUMBER = DIGIT , { DIGIT } ;

    DIGIT = ( 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 0 ) ;

    TYPE = $_719_0 | $_719_1;

    DECLARATION = TYPE, IDENT, ';';

`

# Reserved identifiers

| Symbol 	        | C Equivalent                          |
|:-----------------:|:-------------------------------------:|
| $_436_0        	|  if        	                        |
| $_436_1       	|  else          	                    |
| $_436_2       	|  while      	                        |
| $_436_3       	|  printf      	                        |
| $_436_4       	|  scanf      	                        |
| $_719_0       	|  int      	                        |
| $_719_1       	|  str      	                        |
| $_719_2       	|  void      	                        |
