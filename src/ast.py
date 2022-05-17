class SymbolTable():
    def __init__(self):
        self._table = {}
        # self._reservedWords = ['printf', 'while', 'if', 'else', 'scanf']

    # def isReserved(self, name):
    #     return name in self._reservedWords

    # def declare(self, name, typ):
    #     if name in self._table.keys():
    #         raise Exception(f"Variable {name} already declared")
    #     self._table[name] = (None, typ)
        
    def assign(self, name, value):
        # if name not in self._table.keys():
        #     raise Exception(f"Local variable {name} assigned before declaration")
        self._table[name] = value       

    def retrieve(self, name):
        try:
            return self._table[name]
        except Exception:
            raise NameError("Variable '{0}' referenced before assignment".format(name))


ST = SymbolTable()

class Number():
    def __init__(self, value) -> None:
        self.value = value

    def eval(self):
        return int(self.value)

## Bin Ops
class BinOp():
    def __init__(self, lhs, rhs) -> None:
        self.lhs = lhs
        self.rhs = rhs

class Sum(BinOp):
    def eval(self):
        return self.lhs.eval()+self.rhs.eval()

class Sub(BinOp):
    def eval(self):
        return self.lhs.eval()-self.rhs.eval()

class Mult(BinOp):
    def eval(self):
        return self.lhs.eval()*self.rhs.eval()

class Div(BinOp):
    def eval(self):
        return self.lhs.eval()//self.rhs.eval()

class LT(BinOp):
    def eval(self):
        return int(self.lhs.eval()<self.rhs.eval())

class GT(BinOp):
    def eval(self):
        return int(self.lhs.eval()>self.rhs.eval())

class EQ(BinOp):
    def eval(self):
        return int(self.lhs.eval()==self.rhs.eval())

class NE(BinOp):
    def eval(self):
        return int(self.lhs.eval()!=self.rhs.eval())

class LTE(BinOp):
    def eval(self):
        return int(self.lhs.eval()<=self.rhs.eval())

class GTE(BinOp):
    def eval(self):
        return int(self.lhs.eval()>=self.rhs.eval())

class Or(BinOp):
    def eval(self):
        return int(self.lhs.eval() or self.rhs.eval())

class And(BinOp):
    def eval(self):
        return int(self.lhs.eval() and self.rhs.eval())

# Unary Operators
class UnOp():
    def __init__(self, value) -> None:
        self.value = value

class UnSub(UnOp):
    def eval(self):
        return -self.value.eval()

class UnSum(UnOp):
    def eval(self):
        return self.value.eval()

class Negate(UnOp):
    def eval(self):
        return int(not self.value.eval())

class Assign():
    def __init__(self, name, value):
        self.value = value
        self.name = name

    def eval(self):
        ST.assign(self.name, self.value.eval())

class Identifier():
    def __init__(self, name) -> None:
        self.name = name

    def eval(self):
        return ST.retrieve(self.name)

class Print():
    def __init__(self, value) -> None:
        self.value = value

    def eval(self):
        print(self.value.eval())

class Block():
    def __init__(self, stmt) -> None:
        self.children = [stmt]

    def append(self, val):
        self.children.append(val)

    def eval(self):
        [i.eval() for i in self.children]