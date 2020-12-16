from __future__ import annotations
from tokenizer import Token, tokenize
from typing import Union, List, Tuple, NamedTuple, Optional

class RecursiveDescentHelper:
    """ Used to perform recursive descent parsing on a list of tokens """
    __tokens: List[Token]
    __nextIx: int

    def __init__(self, tokens: List[Token]):
        """ Initializes the helper with a list of tokens """
        self.__tokens = tokens 
        self.__nextIx = 0

    def isNotFinished(self) -> bool:
        """ Returns true iff there are more tokens to process """
        return self.__nextIx < len(self.__tokens)

    def peekNextToken(self) -> Optional[Token]:
        """ Returns the next token, if exists, without advancing the internal pointer """
        if self.isNotFinished():
            return self.__tokens[self.__nextIx]
        return None

    def advanceNextToken(self) -> Optional[Token]:
        """ Advances to the next token, returning it """
        token = self.peekNextToken()
        if token is not None:
            self.__nextIx += 1
        return token





BINARY_OPS = [ '+', '-']


class VariableTerm(NamedTuple):
    variable: str

class ExpressionTerm(NamedTuple):
    expression: Expression

Term = Union[VariableTerm, ExpressionTerm]




def parse_term(rd: RecursiveDescentHelper) -> Term:
    if rd.peekNextToken().type == "identifier":
        return VariableTerm(rd.advanceNextToken().value)
    if rd.peekNextToken().value == "(":
        return parse_expression_term(rd)

def parse_expression_term(rd: RecursiveDescentHelper) -> ExpressionTerm:
    lParen = rd.advanceNextToken()
    assert lParen.value == "("

    expr = parse_expression(rd)

    rParen = rd.advanceNextToken()
    assert rParen.value == ")"

    return ExpressionTerm(expression = expr)


class Expression(NamedTuple):
    term: Term 
    opsWithTerms: List[Tuple[str, Term]]

def parse_expression(rd: RecursiveDescentHelper) -> Expression:
    firstTerm = parse_term(rd)
    
    opTerms = []
    while rd.isNotFinished() and rd.peekNextToken().value in BINARY_OPS:
        op = rd.advanceNextToken().value
        term = parse_term(rd)
        opTerms.append((op, term))
    
    return Expression(
        term = firstTerm,
        opsWithTerms = opTerms
    )

if __name__ == "__main__":
    rd = RecursiveDescentHelper(tokenize("5 + (6 + (7 + 8))"))
    expr = parse_expression(rd)
    print(expr)
    
