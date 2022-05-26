from lexer import Lexer
from parser import Parser
from ast import SymbolTable
import sys

if __name__ == '__main__':
    in_list = [
        '{$_436_3(1);}', # Print 1
        '{$0=1;$_436_3(1);}', # Assign 1 to variable then print it
        '{$0=0;$1=1;$_436_3($0+$1);}', # Assign 0 to x, 1 to y and then print their sum (1)
        '{$_436_0(1){$_436_3(1);}$_436_1{$_436_3(0);}}', # If true print 1 else print 0
        '{$_436_0(0){$_436_3(1);}$_436_1{$_436_3(0);}}', # If false print 1 else print 0
        '{$0=5;$_436_2($0>0){$_436_3($0);$0=$0-1;}}', # X=5; while x>0 print(x), x--
        '''
        {
            $1 = 0;
            $0 = 3;
            $_436 $101() {
                $0 = 1;
                $_436_3($0);
                $_436_3($1);
            }
            $_436_3($0);
            $_436_3($1);
            $101();
        }
        ''', # Test scope of variables function def/call - Output should be 3, 0, 1, 0
        '''
        {
            $0 = 5;
            $_436 $1008($9,$10){
                $_436_2($9 > 0){
                    $_436_3($9);
                    $9 = $9 - 1;
                }
            }
            $1008($0, 0);
        }
        ''', # Function that loops through i=5;i>0;i-- printing i
        '''
        {
            $0 = 100;
            $1 = 90;
            $_436 $1008($9,$10){
                $_436_2($9 > $10){
                    $_436_3($9);
                    $9 = $9 - 1;
                }
            }
            $1008($0, $1);
        }
        ''', # Function that loops through i=x;i>y;i-- printing i
        '''
        {
            $_436 $1008(){
                $_436_4 10 ;
            }
            $0 = $1008();
            $_436_3($0);
        }
        ''', # Function with no arguments that returns 10;
        '''
        {
            $_436 $1008($0){
                $_436_4 $0 + 1 ;
            }
            $0 = $1008(2);
            $_436_3($0);
        }
        ''', # Function with one argument that returns argument plus one;
        '''
        {
            $_436 $1008($0, $2){
                $_436_4 $0 * $2 ;
            }
            $0 = $1008(2, 10);
            $_436_3($0);
        }
        ''', # Function with two arguments that returns their product;
        '''
        {
            $_436 $1008($0){
                $_436_0($0 > 0){
                    $_436_3($0);
                    $1008($0 - 1);
                }
                $_436_3($0);
            }
            $1008(10);
        }
        ''', # Recursive function, that counts from input down to 0, then back up to input.
    ]

    Global_ST = SymbolTable()
    if len(sys.argv) < 2:
        for text_input in in_list:
            # Create lexer
            lexer = Lexer().get_lexer()
            tokens = lexer.lex(text_input)
            print('\nEXPERIMENT:\n', text_input)
            # print('\nTokens:', list(lexer.lex(text_input)))
            # Create parser
            pg = Parser()
            pg.parse()
            parser = pg.get_parser()
            ast = parser.parse(tokens)
            # print(ast)
            ast.eval(Global_ST)
            # print('\n', Global_ST._table)
    else:
        if not sys.argv[1].endswith('.ns'):
            raise Exception("Provided file is not of correct extension! Must be [file].ns, provided {0}".format(sys.argv[1]))
        with open(sys.argv[1], 'r') as f:
            text_input = f.read()
        lexer = Lexer().get_lexer()
        tokens = lexer.lex(text_input)
        pg = Parser()
        pg.parse()
        parser = pg.get_parser()
        ast = parser.parse(tokens)
        ast.eval(Global_ST)