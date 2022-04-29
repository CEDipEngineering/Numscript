# Numscript
My own programming language, using only symbols and numbers. Meant to be programmed using only a numpad and a few extra symbols.

# EBNF

BLOCK = "{", { STATEMENT }, "}" ;

STATEMENT = ( λ | ASSIGNMENT | PRINT), ";" ;

ASSIGNMENT = IDENTIFIER, "=", EXPRESSION ;

PRINT = "$_437_4", "(", EXPRESSION, ")" ;

EXPRESSION = TERM, { ("+" | "-"), TERM } ;

TERM = FACTOR, { ("*" | "/"), FACTOR } ;

FACTOR = (("+" | "-"), FACTOR) | NUMBER | "(", EXPRESSION, ")" | IDENTIFIER ;

IDENTIFIER = $, { DIGIT | "_" } ;

NUMBER = DIGIT, { DIGIT } ;

DIGIT = ( 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 0 ) ;

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
