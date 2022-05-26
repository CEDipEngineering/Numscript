# Numscript
My own programming language, using only symbols and numbers. Meant to be programmed using only a numpad and a few extra symbols.

Given the reduced amount of symbols, this language can become rather fast to use with enough practice.

Also worth noting, is the complete lack of letters, which implies complete lack of words, which in turn means that this language does not require prior knowledge of english, or any other language, and can be written in basically any keyboard layout with indo-arabic numerals and some common symbols for maths, such as '+', '-', '*', '/', '$', '{', '}', ',', ';', '(', ')', etc.

For this example, only integers were implemented, however, floats would not be too difficult to add later. Also, no string type exists, as a language with no text or letter-characters really shouldn't have a type for text and letters. A function such as scanf was not implemented, but would be very similar to print, and would not add much value to the capabilities.

In main.py, there are several examples of codes in my language, that have a small comment explaining their functionality.

To try it out, simply install python and the [rply library](https://pypi.org/project/rply/) (pip install rply), then execute main.py.

If you want to try your own programs, you can write them with the extension '.ns' (as in NumScript), and pass them over to main.py via cmdline arguments (python3 main.py main.ns)

Inspired by Marcelo Andrade's [Tupy](https://github.com/marcelogdeandrade/TupyLanguange)

# EBNF

    BLOCK = '{' , { STATEMENT }, '}' ;

    FUNCDEF = $_436 , IDENTIFIER, '(', λ | (TYPE, IDENTIFIER, {',', TYPE, IDENTIFIER}), ')', FUNCBLOCK ; 

    FUNCBLOCK = '{', {FUNCSTATEMENT}, '}' ;

    FUNCSTATEMENT = (STATEMENT | $_436_5, RELEXPRESSION, ';' );

    STATEMENT = ( λ | ASSIGNMENT | PRINT | DECLARATION | CALL), ';';
                | (BLOCK | WHILE | IF | FUNCDEF);
    
    WHILE = '$_436_2', '(', RELEXPRESSION ,')', STATEMENT;

    IF = '$_436_0', '(', RELEXPRESSION ,')', STATEMENT, ( ( '$_436_1', STATEMENT ) | λ );

    ASSIGNMENT = IDENTIFIER, '=' , EXPRESSION, ';' ;

    RELEXPRESSION = EXPRESSION | EXPRESSION , ( '<' | '>' | '==' | '!=' | '<=' | '>=') , EXPRESSION ;
    
    EXPRESSION = TERM, { ( '+' | '-' | '||' ), TERM } ;
    
    TERM = FACTOR, { ( '*' | '/' | '&&' ), FACTOR } ;
    
    FACTOR =  NUMBER 
            | CALL
            | IDENTIFIER  
            | ( ( '+' | '-' | '!' ) , FACTOR )  
            | '(' , RELEXPRESSION , ')' 
            ;

    CALL = IDENT, '(', λ | (RELEXPRESSION, {',', RELEXRESSION}) , ')';

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
| $_436_4       	|  return      	                        |
| $_436            	|  def      	                        |