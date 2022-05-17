from lexer import Lexer
from parser import Parser

if __name__ == '__main__':

    in_list = [
        '{$_436_3(1);}', # Print 1
        '{$0=1;$_436_3(1);}', # Assign 1 to variable then print it
        '{$0=0;$1=1;$_436_3($0+$1);}', # Assign 0 to x, 1 to y and then print their sum (1)
    ]
            
    for text_input in in_list:
        # Create lexer
        lexer = Lexer().get_lexer()
        tokens = lexer.lex(text_input)
        print('\nEXPERIMENT:\n', text_input)
        print('Tokens:', list(lexer.lex(text_input))[:3], '...')
        # Create parser
        pg = Parser()
        pg.parse()
        parser = pg.get_parser()
        print(f'Output: {parser.parse(tokens).eval()}')