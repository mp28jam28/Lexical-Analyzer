import ply.lex as lex
import re
import os
import sys

# List of token names
tokens = [
    'KEYWORD',
    'SEPARATOR',
    'IDENTIFIER',
    'OPERATOR',
    'NUMBER'
]

# Reserved Keywords
reserved = {
    'if': 'KEYWORD',
    'else': 'KEYWORD',
    'while': 'KEYWORD',
    'return': 'KEYWORD'
}

# Regular expression rules for simple tokens
t_SEPARATOR = r'[()\{\};]'
t_OPERATOR = r'[\+\-\*/=<>!&|]+'

# Identifier (Variable Names)
def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'IDENTIFIER')  # Check for keywords
    return t

# Number (Integer)
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Ignore whitespace and comments
t_ignore = ' \t'
t_ignore_COMMENT = r'//.*'

# Newline tracking
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Error handling
def t_error(t):
    print(f"Illegal character '{t.value[0]}' at line {t.lineno}")
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

# Function to process input file
def accept_file(filename):
    if not os.path.exists(filename):
        print("Error: File not found.")
        return
    
    with open(filename, 'r') as file:
        data = file.read()
        lexer.input(data)

# Function to print output tokens
def print_output():
    for token in lexer:
        print(f"{token.value} = {token.type}")

# Main execution
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python lexer.py <filename>")
        sys.exit(1)

    input_file = sys.argv[1]
    accept_file(input_file)
    print_output()
