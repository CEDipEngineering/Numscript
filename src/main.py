from lexer import Lexer
from parser import Parser

if __name__ == '__main__':

    in_list = ['1',
               '1+1',
               '1-1',
               '2*3',
               '2/1',
               '10/5',
               '2>1',
               '2==1',
               '2==1+1',
               '1+(1+1)+2',
               '2*(1+1)',
               '1>2*(10+10)'   
            ]
            
    for text_input in in_list:
        # Create lexer
        lexer = Lexer().get_lexer()
        tokens = lexer.lex(text_input)
        print('\nEXPERIMENT:\n', text_input)
        print('Tokens:', list(lexer.lex(text_input)))
        # Create parser
        pg = Parser()
        pg.parse()
        parser = pg.get_parser()
        print(f'Output: {parser.parse(tokens).eval()}')