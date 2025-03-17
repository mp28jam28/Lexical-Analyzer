import re

# Define token specifications in order of priority (longer operators before shorter ones)
token_specification = [
    ('COMMENT', r'//.*'),  # Single-line comment
    ('KEYWORD', r'\b(if|else|return|for|while|do|break|continue)\b'),
    ('INTEGER', r'\b\d+\b'),
    ('IDENTIFIER', r'\b[a-zA-Z_]\w*\b'),
    ('OPERATOR', r'==|>=|<=|!=|>|<|=|\+|-|\*|/'),
    ('SEPARATOR', r'[\(\)\{\}\[\];,]'),
    ('WHITESPACE', r'\s+'),
    ('MISMATCH', r'.'),  # Any other character
]

# Combine the regex patterns into a master pattern.
token_regex = '|'.join('(?P<%s>%s)' % pair for pair in token_specification)
compiled_regex = re.compile(token_regex)


def tokenize(code):
    tokens = []
    # Scan through the input code using the regex.
    for mo in compiled_regex.finditer(code):
        kind = mo.lastgroup
        value = mo.group(kind)
        if kind in ('WHITESPACE', 'COMMENT'):
            # Skip whitespace and comments
            continue
        elif kind == 'MISMATCH':
            raise RuntimeError(f'Unexpected character {value!r}')
        tokens.append((value, kind))
    return tokens


if __name__ == "__main__":
    # Read the input from a .txt file (change 'input.txt' to your filename)
    with open('input.txt', 'r') as f:
        code = f.read()

    # Tokenize the input code
    tokens = tokenize(code)

    # Output lexemes and corresponding token types
    print("Lexeme".ljust(15), "Token")
    print("-" * 30)
    for lexeme, token in tokens:
        print(f"{lexeme.ljust(15)} {token}")
