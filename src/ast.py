
class SymbolTable():
    def __init__(self, ST = None):
        if ST is None:
            self._table = {}
        else:
            self._table = dict(ST._table) # Force a copy, beacuse python
        
    def assign(self, name, value):
        self._table[name] = value       

    def retrieve(self, name):
        try:
            return self._table[name]
        except Exception:
            raise NameError("Variable '{0}' referenced before assignment".format(name))

class Number():
    def __init__(self, value) -> None:
        self.value = value

    def eval(self, ST):
        return int(self.value)

## Bin Ops
class BinOp():
    def __init__(self, lhs, rhs) -> None:
        self.lhs = lhs
        self.rhs = rhs

class Sum(BinOp):
    def eval(self, ST):
        return self.lhs.eval(ST)+self.rhs.eval(ST)

class Sub(BinOp):
    def eval(self, ST):
        return self.lhs.eval(ST)-self.rhs.eval(ST)

class Mult(BinOp):
    def eval(self, ST):
        return self.lhs.eval(ST)*self.rhs.eval(ST)

class Div(BinOp):
    def eval(self, ST):
        return self.lhs.eval(ST)//self.rhs.eval(ST)

class LT(BinOp):
    def eval(self, ST):
        return int(self.lhs.eval(ST)<self.rhs.eval(ST))

class GT(BinOp):
    def eval(self, ST):
        return int(self.lhs.eval(ST)>self.rhs.eval(ST))

class EQ(BinOp):
    def eval(self, ST):
        return int(self.lhs.eval(ST)==self.rhs.eval(ST))

class NE(BinOp):
    def eval(self, ST):
        return int(self.lhs.eval(ST)!=self.rhs.eval(ST))

class LTE(BinOp):
    def eval(self, ST):
        return int(self.lhs.eval(ST)<=self.rhs.eval(ST))

class GTE(BinOp):
    def eval(self, ST):
        return int(self.lhs.eval(ST)>=self.rhs.eval(ST))

class Or(BinOp):
    def eval(self, ST):
        return int(self.lhs.eval(ST) or self.rhs.eval(ST))

class And(BinOp):
    def eval(self, ST):
        return int(self.lhs.eval(ST) and self.rhs.eval(ST))

# Unary Operators
class UnOp():
    def __init__(self, value) -> None:
        self.value = value

class UnSub(UnOp):
    def eval(self, ST):
        return -self.value.eval(ST)

class UnSum(UnOp):
    def eval(self, ST):
        return self.value.eval(ST)

class Negate(UnOp):
    def eval(self, ST):
        return int(not self.value.eval(ST))

class Assign():
    def __init__(self, name, value):
        self.value = value
        self.name = name

    def eval(self, ST):
        ST.assign(self.name, self.value.eval(ST))

class Identifier():
    def __init__(self, name) -> None:
        self.name = name

    def eval(self, ST):
        return ST.retrieve(self.name)

class Print():
    def __init__(self, value) -> None:
        self.value = value

    def eval(self, ST):
        print(self.value.eval(ST))

class Block():
    def __init__(self, stmt) -> None:
        self.children = [stmt]

    def append(self, val):
        self.children.append(val)

    def eval(self, ST):
        [i.eval(ST) for i in self.children]

    def __str__(self):
        return f'Block: {self.children}'

class If():
    def __init__(self, cond, s1) -> None:
        self.cond = cond
        self.true_stmt = s1
    
    def eval(self, ST):
        tf = self.cond.eval(ST)
        if(tf):
            self.true_stmt.eval(ST)

class NoOp():
    def __init__(self) -> None:
        pass

    def eval():
        pass

class IfElse():
    def __init__(self, cond, s1, s2) -> None:
        self.cond = cond
        self.true_stmt = s1
        self.false_stmt = s2
    
    def eval(self, ST):
        tf = self.cond.eval(ST)
        if(tf):
            self.true_stmt.eval(ST)
        else:
            self.false_stmt.eval(ST)

class While():
    def __init__(self, cond, s) -> None:
        self.cond = cond
        self.stmt = s

    def eval(self, ST):
        while(self.cond.eval(ST)):
            self.stmt.eval(ST)

class Def():
    def __init__(self, name, args, block) -> None:
        self.name = name
        self.block = block
        if args:
            self.args = [args]
        else:
            self.args = []

    def args_append(self, val):
        self.args.append(val)

    def eval(self, ST):
        # print(f'Function defined with: {self.args=},{str(self.block)=}')
        ST.assign(self.name, (self.args, self.block))

class Call():
    def __init__(self, name, params) -> None:
        self.name = name
        if params:
            self.params = [params]
        else:
            self.params = []

    def params_append(self, val):
        self.params.append(val)

    def eval(self, ST):
        func = ST.retrieve(self.name)
        args, block = func
        if len(args) != len(self.params):
            raise Exception("Invalid Function Call")
        ST_func = SymbolTable(ST)
        if len(self.params) != 0:
            # print(f'{self.params=}')
            for arg, par in zip(args[0], self.params[0]):
                # print(arg, par)
                ST_func.assign(arg, par.eval(ST))
        # print(block.children)
        block.eval(ST_func)
