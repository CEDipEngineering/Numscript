from lexer import Lexer
from parser import Parser
from ast import SymbolTable

if __name__ == '__main__':

    Global_ST = SymbolTable()
    in_list = [
        # '{$_436_3(1);}', # Print 1
        # '{$0=1;$_436_3(1);}', # Assign 1 to variable then print it
        # '{$0=0;$1=1;$_436_3($0+$1);}', # Assign 0 to x, 1 to y and then print their sum (1)
        # '{$_436_0(1){$_436_3(1);}$_436_1{$_436_3(0);}}', # If true print 1 else print 0
        # '{$_436_0(0){$_436_3(1);}$_436_1{$_436_3(0);}}', # If false print 1 else print 0
        # '{$0=5;$_436_2($0>0){$_436_3($0);$0=$0-1;}}', # X=5; while x>0 print(x), x--
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
        ''',
    ]
            
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
        print(f'\nOutput: {parser.parse(tokens).eval(Global_ST)}')
        # print('\n', Global_ST._table)