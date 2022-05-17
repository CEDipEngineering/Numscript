# Numscript
My own programming language, using only symbols and numbers. Meant to be programmed using only a numpad and a few extra symbols.

Given the reduced amount of symbols, this language can become rather fast to use with enough practice.

Also worth noting, is the complete lack of letters, which implies complete lack of words, which in turn means that this language does not require prior knowledge of english, or any other language, and can be written in basically any keyboard layout with indo-arabic numerals and some common symbols for maths, such as '+', '-', '*', '/', '$', '{', '}', ',', ';', '(', ')', etc.

Inspired by Marcelo Andrade's (Tupy)[https://github.com/marcelogdeandrade/TupyLanguange]

# EBNF

    BLOCK = '{' , { STATEMENT }, '}' ;

    FUNCTION = $_436 , IDENTIFIER, '(', TYPE, IDENTIFIER, {',', TYPE, IDENTIFIER}, ')', BLOCK ; 

    STATEMENT = ( λ | ASSIGNMENT | PRINT | DECLARATION | $_436_5, RELEXPRESSION ), ';';
                | (BLOCK | WHILE | IF | FUNCTION);

    FACTOR = NUMBER 
            | IDENTIFIER  
            | ( ( '+' | '-' | '!' ) , FACTOR )  
            | '(' , RELEXPRESSION , ')'
            | CALL;

    CALL = IDENT, '(', λ | RELEXPRESSION, {',', RELEXRESSION}, ')', ';';

    EXPRESSION = TERM, { ( '+' | '-' | '||' ), TERM } ;

    TERM = FACTOR, { ( '*' | '/' | '&&' ), FACTOR } ;

    RELEXPRESSION = EXPRESSION | EXPRESSION , ( '<' | '>' | '==' | '!=' | '<=' | '>=') , EXPRESSION ;

    WHILE = '$_436_2', '(', RELEXPRESSION ,')', STATEMENT;

    IF = '$_436_0', '(', RELEXPRESSION ,')', STATEMENT, ( ( '$_436_1', STATEMENT ) | λ );

    ASSIGNMENT = IDENTIFIER, '=' , EXPRESSION, ';' ;

    PRINT = '$_436_3', '(' , EXPRESSION, ')' ;

    IDENTIFIER = $, DIGIT | '_', { DIGIT | '_' } ;

    NUMBER = DIGIT , { DIGIT } ;

    DIGIT = ( 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 0 ) ;


# Reserved identifiers

| Symbol 	        | Python Equivalent                          |
|:-----------------:|:-------------------------------------:|
| $_436_0        	|  if        	                        |
| $_436_1       	|  else          	                    |
| $_436_2       	|  while      	                        |
| $_436_3       	|  print      	                        |
| $_436_5       	|  return      	                        |
| $_436            	|  def      	                        |