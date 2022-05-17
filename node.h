#include <iostream>
#include <vector>
// #include <llvm/Value.h>

// class CodeGenContext;
class NStatement;
class NExpression;
class NVariableDeclaration;

typedef std::vector<NStatement*> StatementList;
typedef std::vector<NVariableDeclaration*> VariableList;
typedef std::vector<NExpression*> ExpressionList;

class Node {
public:
    virtual ~Node() {}
    // virtual llvm::Value* codeGen(CodeGenContext& context) { }
};

class NBlock : public Node {
public:
    StatementList statements;
    NBlock(const StatementList& statements) : statements(statements) { }
    // virtual llvm::Value* codeGen(CodeGenContext& context);
};

class NStatement : public Node { };

class NFunctionDeclaration : public NStatement {
public:
    const NIdentifier& type;
    const NIdentifier& id;
    VariableList arguments;
    NBlock& block;
    NFunctionDeclaration(const NIdentifier& type, const NIdentifier& id, 
            const VariableList& arguments, NBlock& block) :
        type(type), id(id), arguments(arguments), block(block) { }
    // virtual llvm::Value* codeGen(CodeGenContext& context);
};

class NMethodCall : public NExpression {
public:
    const NIdentifier& id;
    ExpressionList arguments;
    NMethodCall(const NIdentifier& id, ExpressionList& arguments) :
        id(id), arguments(arguments) { }
    NMethodCall(const NIdentifier& id) : id(id) { }
    // virtual llvm::Value* codeGen(CodeGenContext& context);
};



/*
// BLOCK
// FUNCTION
// STATEMENT
// FACTOR
// CALL
TERM
EXPRESSION
RELEXPRESSION
WHILE
IF
ASSIGNMENT
PRINT
IDENTIFIER
TYPE
DECLARATION
*/