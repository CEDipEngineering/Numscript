from logging.config import IDENTIFIER
from sre_constants import ASSERT
from rply import ParserGenerator
from ast import (Sum, Number, Sub, Mult, 
                 Div, GT, LT, EQ, NE, GTE, 
                 LTE, Or, And, UnSum, UnSub, 
                 Negate, Identifier, Assign, 
                 Print, Block, If, NoOp, IfElse, 
                 While, Def, Call, Funcblock, Return)

class Parser():
    def __init__(self):
        self.curr = ""
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
             'IDENTIFIER',
             'ASSIGN', 
             'SEMICOL', 
             'OCB', 
             'CCB', 
             'PRINT', 
             'IF', 
             'ELSE', 
             'WHILE', 
             'DEF', 
             'COMMA',
             'RETURN',
             ],
             precedence=[
                 ("left", ["funcblock", "block"]),
             ]
        )

    def parse(self):

        #########
        #-Block-#
        #########
        @self.pg.production('block : OCB statements CCB')
        def block(p):
            self.curr = "block"
            return p[1]
        
        @self.pg.production('statements : statement')
        def statements(p):
            self.curr = "statements"
            return Block(p[0])
        
        @self.pg.production('statements : statements statement')
        def statements(p):
            self.curr = "statements"
            p[0].append(p[1])
            return p[0]

        #############
        #-Statement-#
        #############
        @self.pg.production('statement : SEMICOL')
        def statement(p):
            self.curr = "statement"
            return NoOp()

        # Funcdef statement
        @self.pg.production('statement : funcdef')
        def statement(p):
            self.curr = "statement"
            return p[0]

        @self.pg.production('statement : call')
        def statement(p):
            self.curr = "statement"
            return p[0]

        # Assignment statement
        @self.pg.production('statement : assignment')
        def statement(p):
            self.curr = "statement"
            return p[0]

        # Block statement
        @self.pg.production('statement : block')
        def statement(p):
            self.curr = "statement"
            return p[0]

        #######
        #-Def-#
        #######
        @self.pg.production('funcdef : DEF IDENTIFIER OP identifiers CP funcblock')
        def funcdef(p):
            self.curr = "funcdef"
            return Def(p[1].getstr(), p[3], p[5])

        @self.pg.production('funcblock : OCB funcstatements CCB')
        def funcblock(p):
            self.curr = "funcblock"
            return p[1]

        @self.pg.production('funcstatements : funcstatement')
        def funcstatements(p):
            self.curr = "funcstatements"
            return Funcblock(p[0])
        
        @self.pg.production('funcstatement : RETURN relexpr SEMICOL')
        def funcstatement(p):
            self.curr = "funcstatement"
            return Return(p[1])

        @self.pg.production('funcstatement : statement')
        def funcstatement(p):
            self.curr = "funcstatement"
            return p[0]

        @self.pg.production('funcstatement : funcstatements statement')
        def funcstatement(p):
            self.curr = "funcstatement"
            p[0].append(p[1])
            return p[0]
        

        # Function with no args
        @self.pg.production('funcdef : DEF IDENTIFIER OP CP funcblock')
        def funcdef(p):
            self.curr = "funcdef"
            return Def(p[1].getstr(), 0, p[4])

        @self.pg.production('identifiers : IDENTIFIER')
        def identifiers(p):
            self.curr = "identifiers"
            return [p[0].getstr()]
        
        @self.pg.production('identifiers : identifiers COMMA IDENTIFIER')
        def identifiers(p):
            self.curr = "identifiers"
            p[0].append(p[2].getstr())
            return p[0]
        
        #########
        #-Print-#
        #########
        @self.pg.production('statement : PRINT OP relexpr CP SEMICOL')
        def statement(p):
            self.curr = "statement"
            return Print(p[2])

        ##########
        #-IfElse-#
        ##########
        @self.pg.production('statement : IF OP relexpr CP statement ELSE statement')
        def statement(p):
            self.curr = "statement"
            return IfElse(p[2], p[4], p[6])

        ######
        #-If-#
        ######
        @self.pg.production('statement : IF OP relexpr CP statement')
        def statement(p):
            self.curr = "statement"
            return If(p[2], p[4])

        #########
        #-While-#
        #########
        @self.pg.production('statement : WHILE OP relexpr CP statement')
        def statement(p):
            self.curr = "statement"
            return While(p[2], p[4])

        ########
        #-Call-#
        ########
        @self.pg.production('call : IDENTIFIER OP relexprs CP SEMICOL')
        def factor(p):
            self.curr = "call"
            return Call(p[0].getstr(), p[2])

        @self.pg.production('call : IDENTIFIER OP CP SEMICOL')
        def factor(p):
            self.curr = "call"
            return Call(p[0].getstr(), 0)

        @self.pg.production('relexprs : relexpr')
        def relexprs(p):
            self.curr = "relexprs"
            return [p[0]]
        
        @self.pg.production('relexprs : relexprs COMMA relexpr')
        def relexprs(p):
            self.curr = "relexprs"
            p[0].append(p[2])
            return p[0]

        ##############
        #-Assignment-#
        ##############
        @self.pg.production('assignment : IDENTIFIER ASSIGN relexpr SEMICOL')
        def assignment(p):
            self.curr = "assignment"
            ident = p[0].getstr()
            val = p[2]
            return Assign(ident, val)


        ###########
        #-Relexpr-#
        ###########
        # Single token
        @self.pg.production('relexpr : expression')
        def relexpr(p):
            self.curr = "relexpr"
            return p[0]

        # Three tokens (there is no A > B > C)
        @self.pg.production('relexpr : expression GT expression')
        @self.pg.production('relexpr : expression LT expression')
        @self.pg.production('relexpr : expression EQ expression')
        @self.pg.production('relexpr : expression NE expression')
        @self.pg.production('relexpr : expression LTE expression')
        @self.pg.production('relexpr : expression GTE expression')
        def relexpr(p):
            self.curr = "relexpr"
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
            self.curr = "expression"
            return p[0]

        # Nested expressions
        @self.pg.production('expression : term PLUS expression')
        @self.pg.production('expression : term MINUS expression')
        @self.pg.production('expression : term OR expression')
        def expression(p):
            self.curr = "expression"
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
            self.curr = "term"
            return p[0]

        # Nested terms
        @self.pg.production('term : factor MUL term')
        @self.pg.production('term : factor DIV term')
        @self.pg.production('term : factor AND term')
        def term(p):
            self.curr = "term"
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
        # Call with return and no args
        @self.pg.production('factor : IDENTIFIER OP CP')
        def factor(p):
            self.curr = "factor"
            return Call(p[0].getstr(), 0)
        
        # Call with return and no args
        @self.pg.production('factor : IDENTIFIER OP relexprs CP')
        def factor(p):
            self.curr = "factor"
            return Call(p[0].getstr(), p[2])


        # Single token
        @self.pg.production('factor : NUMBER')
        @self.pg.production('factor : IDENTIFIER')
        def factor(p):
            self.curr = "factor"
            valType = p[0].gettokentype()
            if valType == 'NUMBER':
                return Number(p[0].getstr())
            elif valType == 'IDENTIFIER':
                return Identifier(p[0].getstr()) 
            else:
                raise Exception('This is bad too m8')

        # Unary operators
        @self.pg.production('factor : MINUS factor')
        @self.pg.production('factor : PLUS factor')
        @self.pg.production('factor : NOT factor')
        def factor(p):
            self.curr = "factor"
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
            self.curr = "factor"
            return p[1]       

        @self.pg.error
        def error_handle(token):
            print(self.curr)
            raise ValueError(token)

    def get_parser(self):
        return self.pg.build()