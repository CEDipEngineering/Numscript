from rply import LexerGenerator


class Lexer():
    def __init__(self):
        self.lexer = LexerGenerator()

    def _add_tokens(self):

        # Types and Values
        # self.lexer.add('INT', r'$_157')
        self.lexer.add('NUMBER', r'\d+')
        # self.lexer.add('SEMICOL', r'\;')
        # self.lexer.add('IDENTIFIER', r'\$[0-9_]+')

        # Arithmetic
        self.lexer.add('MUL', r'\*')
        self.lexer.add('DIV', r'/')
        self.lexer.add('PLUS', r'\+')
        self.lexer.add('MINUS', r'-')
        
        # Logic
        self.lexer.add('GT', r'\>')
        self.lexer.add('LT', r'\<')
        self.lexer.add('EQ', r'\=\=')
        self.lexer.add('NE', r'\!\=')
        self.lexer.add('LTE', r'\<\=')
        self.lexer.add('GTE', r'\>\=')
        self.lexer.add('NOT', r'\!')
        self.lexer.add('OP', r'\(')
        self.lexer.add('CP', r'\)')
        # self.lexer.add('OCB', r'\{')
        # self.lexer.add('CCB', r'\}')
        self.lexer.add('OR', r'\|\|')
        self.lexer.add('AND', r'\&\&')

        # Reserved
        # self.lexer.add('ASSIGN', r'\=')
        # self.lexer.add('IF', r'$_436_0')
        # self.lexer.add('ELSE', r'$_436_1')
        # self.lexer.add('WHILE', r'$_436_2')
        # self.lexer.add('PRINT', r'$_436_3')
        # self.lexer.add('RETURN', r'$_436_5')

        self.lexer.ignore('\s+')

    def get_lexer(self):
        self._add_tokens()
        return self.lexer.build()