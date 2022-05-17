from rply import ParserGenerator
from ast import *


class Parser():
    def __init__(self, builder, module, print_func):
        self.pg = ParserGenerator(
            # A list of all token names, accepted by the parser.
            ['INT', 'NUMBER', 'SEMICOL', 'IDENTIFIER',
             'MUL', 'DIV', 'PLUS', 'MINUS',
             'GT', 'LT', 'EQ', 'NE', 'LTE', 'GTE',
             'OP', 'CP', 'OCB', 'CCB', 'ASSIGN', 'NOT',
             'IF', 'ELSE', 'WHILE', 'PRINT', 'RETURN'
             ],
        )
        self.builder = builder
        self.module = module
        self.print_func = print_func

    def parse(self):

        # Block
        @self.pg.production('block : OCB statement_list CCB')
        def block(p):
            return p[1]

        @self.pg.production('statement_list : statement')
        def statement_list_one(p):
            return Statements(self.builder, self.module, p[0])

        @self.pg.production('statement_list : statement_list statement')
        def statement_list_more(p):
            p[0].add_child(p[1])
            return p[0]

        # Statement
        # IF
        @self.pg.production('statement : IF OP rel CP OCB statement_list CCB')
        def statement_if(p):
            return If(self.builder, self.module, p[2], p[5])
        # IF + ELSE
        @self.pg.production('statement : IF OP rel CP OCB statement_list CCB ELSE OCB statement_list CCB')
        def statement_if(p):
            return IfElse(self.builder, self.module, p[2], p[5], p[9])

        # VarDec
        @self.pg.production('statement : INT IDENTIFIER SEMICOL')
        def var_dec(p):
            return VarDec(self.builder, self.module, p[1])

        # Assign
        @self.pg.production('statement : IDENTIFIER ASSIGN rel SEMICOL')
        def assign(p):
            left = p[0]
            right = p[2]
            return Assign(self.builder, self.module, left, right)

        # Print
        @self.pg.production('statement : PRINT OP rel CP SEMICOL')
        def print_func(p):
            value = p[2]
            return Print(self.builder, self.module, self.print_func, value)

        # While
        @self.pg.production('statement : WHILE OP rel CP statement')
        def while_loop(p):
            cond = p[2]
            children = p[4]
            return While(self.builder, self.module, cond, children)

        # BlockStatement
        @self.pg.production('statement : block')
        def block_statement(p):
            return p[0]

        # Return
        @self.pg.production('statement : RETURN rel')
        def return_statement(p):
            return Return(self.builder, self.module, p[1])

        # Function
        @self.pg.production('statement : function')
        def function_statement(p):
            return p[0]

        # Factor
        @self.pg.production('factor : NUMBER')
        @self.pg.production('factor : IDENTIFIER')
        @self.pg.production('factor : call')
        def factor(p):
            return p[0]

        @self.pg.production('factor : PLUS factor')
        @self.pg.production('factor : MINUS factor')
        @self.pg.production('factor : NOT factor')        
        def factor(p):
            if p[0].gettokentype() == 'PLUS':
                return UnPlus(self.builder, self.module, p[1])
            elif p[0].gettokentype() == 'MINUS':
                return UnMinus(self.builder, self.module, p[1])
            elif p[0].gettokentype() == 'NOT':
                return UnNot(self.builder, self.module, p[1])
            else:
                raise AssertionError('Oooooo Boy')
                
        @self.pg.production('factor : OP rel CP')        
        def factor(p):
            return p[1]

        
        @self.pg.production('rel : expr')
        def rel(p):
            return Expr(self.builder, self.module, p[0])

        @self.pg.production('rel : expr GT expr')
        @self.pg.production('rel : expr LT expr')
        @self.pg.production('rel : expr EQ expr')
        @self.pg.production('rel : expr NE expr')
        @self.pg.production('rel : expr LTE expr')
        @self.pg.production('rel : expr GTE expr')
        def rel(p):
            left = p[0]
            right = p[2]
            if p[1].gettokentype() == 'GT':
                return GT(self.builder, self.module, left, right)
            elif p[1].gettokentype() == 'LT':
                return LT(self.builder, self.module, left, right)
            elif p[1].gettokentype() == 'EQ':
                return EQ(self.builder, self.module, left, right)
            elif p[1].gettokentype() == 'NE':
                return NE(self.builder, self.module, left, right)
            elif p[1].gettokentype() == 'LTE':
                return LTE(self.builder, self.module, left, right)
            elif p[1].gettokentype() == 'GTE':
                return NE(self.builder, self.module, left, right)
            else:
                raise AssertionError('Oops, this should not be possible!')

        @self.pg.production('statement : expr')
        def statement_expr(p):
            return p[0]

        @self.pg.production('expr : term PLUS term')
        @self.pg.production('expr : term MINUS term')
        def expr_binop(p):
            left = p[0]
            right = p[2]
            if p[1].gettokentype() == 'PLUS':
                return Add(self.builder, self.module, left, right)
            elif p[1].gettokentype() == 'MINUS':
                return Sub(self.builder, self.module, left, right)
            else:
                raise AssertionError('Oops, this should not be possible!')

        @self.pg.production('expr : term')
        def expr_term(p):
            return p[0]

        @self.pg.production('term : factor MUL factor')
        @self.pg.production('term : factor DIV factor')
        def term(p):
            left = p[0]
            right = p[2]
            if p[1].gettokentype() == 'MUL':
                return Mul(self.builder, self.module, left, right)
            elif p[1].gettokentype() == 'DIV':
                return Div(self.builder, self.module, left, right)
            else:
                raise AssertionError('Oops, this should not be possible!')

        @self.pg.production('term : factor')
        def term_factor(p):
            return p[0]

        @self.pg.production('factor : NUMBER')
        def factor_number(p):
            return Number(self.builder, self.module, p[0].getstr())

        @self.pg.production('factor : IDENTIFIER')
        def identifier(p):
            return Identifier(self.builder, self.module, p[0])

        @self.pg.production('factor : OP expr CP')
        def expr_parens(p):
            return p[1]

        @self.pg.production('text : QUOTE IDENTIFIER QUOTE')
        def text(p):
            return p[1]

        @self.pg.error
        def error_handle(token):
            raise ValueError(token)

    def get_parser(self):
        return self.pg.build()