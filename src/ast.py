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