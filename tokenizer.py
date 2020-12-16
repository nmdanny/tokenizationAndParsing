from typing import NamedTuple, List
import re 

class Token(NamedTuple):
    type: str
    value: str


def escape_symbol(s: str) -> str:
    """ Symbols like `{, `}`, `(`, `)` often have special meaning in regex, thus we escape them by
        adding a single backslash. (Two slashes are because Python also interprets a single slash as an escape character) """
    return f"\\{s}"


symbols = [
    '=', '+', '-', '{', '}', '(', ')'
]

symbol_regex = f"(?P<symbol>{'|'.join(escape_symbol(symbol) for symbol in symbols)})"

keywords = [
    'function', 'let', 'var', 'do'
]

keyword_regex = f"(?P<keyword>{'|'.join(keywords)})"

# an identifier is one or more word characters(\w+)
identifier_regex = r"(?P<identifier>\w+)"


# note that an identifier regex can accidentally match keywords too, therefore, when we
# unionize all regexes, we must put the keyword regex BEFORE the identifier regex!
tok_regex = '|'.join([symbol_regex, keyword_regex, identifier_regex])


def tokenize(code: str) -> List[Token]:
    tokens = []
    # note that 'finditer' will simply skip unrecognized elements, like whitespace and newlines
    # This isn't always what we want, if we want to support comments, we should recognize them via a regex, otherwise words in a comment might be interpreted
    # as identifiers/keywords, which is not what we want.
    for match in re.finditer(tok_regex, code):
        token = Token(
            type=match.lastgroup,
            value=match.group()
        )
        tokens.append(token)
    return tokens

if __name__ == '__main__':
    print("Printing important regexes:")
    print("symbol_regex", symbol_regex)
    print("keyword_regex", keyword_regex)
    print("identifier_regex", identifier_regex)
    print("\nThe combined regex, which is an OR of the above regexes, is:\n", tok_regex)
    print()
    exampleCode = """
    function void printPlus(int a, int b) {
        var sum;
        let sum = a + b;
        do printInt(sum);
    }
    """

    exampleTokens = tokenize(exampleCode)
    print("The result of tokenizing the following code:", exampleCode, " is the following tokens:\n", exampleTokens)