from logging.config import IDENTIFIER
from rply import ParserGenerator
from ast import Sum, Number, Sub, Mult, Div, GT, LT, EQ, NE, GTE, LTE, Or, And, UnSum, UnSub, Negate


class Parser():
    def __init__(self):
        self.pg = ParserGenerator(
            # A list of all token names, accepted by the parser.
            [
             'NUMBER', 
             'MUL', 
             'DIV', 
             'PLUS', 
             'MINUS',
             'NOT',
             'AND', 
             'OR',
             'GT', 
             'LT', 
             'EQ', 
             'NE', 
             'LTE', 
             'GTE',
             'OP', 
             'CP', 
            #  'INT', 
            #  'SEMICOL', 
            #  'IDENTIFIER',
            #  'OCB', 
            #  'CCB', 
            #  'ASSIGN', 
            #  'IF', 
            #  'ELSE', 
            #  'WHILE', 
            #  'PRINT', 
            #  'RETURN',
             ]
        )

    def parse(self):


        ###########
        #-Relexpr-#
        ###########
        # Single token
        @self.pg.production('relexpr : expression')
        def relexpr(p):
            return p[0]

        # Three tokens (there is no A > B > C)
        @self.pg.production('relexpr : expression GT expression')
        @self.pg.production('relexpr : expression LT expression')
        @self.pg.production('relexpr : expression EQ expression')
        @self.pg.production('relexpr : expression NE expression')
        @self.pg.production('relexpr : expression LTE expression')
        @self.pg.production('relexpr : expression GTE expression')
        def relexpr(p):
            lhs = p[0]
            rhs = p[2]
            opType = p[1].gettokentype()
            if opType == 'GT':
                return GT(lhs, rhs)
            elif opType == 'LT':
                return LT(lhs, rhs)
            elif opType == 'EQ':
                return EQ(lhs, rhs)
            elif opType == 'NE':
                return NE(lhs, rhs)
            elif opType == 'LTE':
                return LTE(lhs, rhs)
            elif opType == 'GTE':
                return GTE(lhs, rhs)
            else:
                raise Exception("This ain't good m8")


        ##############
        #-Expression-#
        ##############
        # Single token
        @self.pg.production('expression : term')
        def expression(p):
            return p[0]

        # Nested expressions
        @self.pg.production('expression : term PLUS expression')
        @self.pg.production('expression : term MINUS expression')
        @self.pg.production('expression : term OR expression')
        def expression(p):
            lhs = p[0]
            rhs = p[2]
            opType = p[1].gettokentype()
            if opType == 'PLUS':
                return Sum(lhs, rhs)
            elif opType == 'MINUS':
                return Sub(lhs, rhs)
            elif opType == 'OR':
                return Or(lhs, rhs)
            else:
                raise Exception("This ain't good m8")


        ########
        #-Term-#
        ########
        # Single token
        @self.pg.production('term : factor')
        def term(p):
            return p[0]

        # Nested terms
        @self.pg.production('term : factor MUL term')
        @self.pg.production('term : factor DIV term')
        @self.pg.production('term : factor AND term')
        def term(p):
            lhs = p[0]
            rhs = p[2]
            opType = p[1].gettokentype()
            if opType == 'MUL':
                return Mult(lhs, rhs)
            elif opType == 'DIV':
                return Div(lhs, rhs)
            elif opType == 'AND':
                return And(lhs, rhs)
            else:
                raise Exception("This ain't good m8")

        ##########
        #-Factor-#
        ##########
        # Single token
        @self.pg.production('factor : NUMBER')
        # @self.pg.production('factor : IDENTIFIER')
        # @self.pg.production('factor : CALL')
        def factor(p):
            valType = p[0].gettokentype()
            if valType == 'NUMBER':
                return Number(p[0].getstr())
            # elif valType == 'IDENTIFIER':
            #     return 
            # elif valType == 'CALL':
            #     return 
            else:
                raise Exception('This is bad too m8')

        # Unary operators
        @self.pg.production('factor : MINUS factor')
        @self.pg.production('factor : PLUS factor')
        @self.pg.production('factor : NOT factor')
        def factor(p):
            value = p[1]
            opType = p[0].gettokentype()
            if opType == 'MINUS':
                return UnSub(value)
            elif opType == 'PLUS':
                return UnSum(value)
            elif opType == 'NOT':
                return Negate(value)
            else:
                raise Exception("This is even worse m8")

        # Parentheses
        @self.pg.production('factor : OP relexpr CP')
        def factor(p):
            return p[1]

        @self.pg.error
        def error_handle(token):
            raise ValueError(token)

    def get_parser(self):
        return self.pg.build()