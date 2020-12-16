
The grammar is as follows(Might have some similarity to Jack, don't remebmer Jack syntax)

`function type functionName(args) { body }`

- `function` is a keyword, `type` is an identifier, `functionName` is an identifier.
- `(`, `)`, `{`, `}` are symbols
- `args` and `body` are defined as follows:

    - `args`

        - A list of 0 or more arguments, where each argument is `type name`, where both `type` and `name` are identifiers

    - `body`
        - A list of 0 or more statements, where each statement will be defined shortly
          (variable statements can only appear at the beginning, this means, they cannot appear after other types of statements)


- A statement is one of the following:
    - A `var` statement, which is a variable declaration, and is of the form
        `var type variableName;` where `var` is a keyword, `type` and `variableName` are identifiers
    - A `do` statement, which is a function call
        - `do functionName(callArgs);` where `do` is a keyword and `functionName` is an identifier, `(`, `)` are symbols
        - `callArgs` is a list of 0 or more identifiers(similar to `args`, but no need to specify types)

    - A `let` statement, which is a variable assignment
        - `let variableName = expression;`
        - `let` is a keyword, `variableName` is an identifier, `=` is a symbol, `expression` is defined below


    - There are more statements like `if`, `while` which I'll omit for simplicity

- An expression is one of the following:

    - Variable, e.g `variableName` which is an identifier
    - A binary assignment of two expressions, e.g, `expression1 + expression2`, where both `expression1` and `expression2` are expressions, and `+` is a symbol


