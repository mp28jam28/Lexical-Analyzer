import ply.lex
import re
import os
import sys

# FUNCTIONS FOR IDENTIFYING TOKENS
def t_KEYWORD(t): pass

def t_SEPARATION(t): pass

def t_IDENTIFIER(t): pass

def t_OPERATOR(t): pass

def t_NUMBER(t):
    r'\d+' # digit character
    t.value = int(t.value)
    return t


# DICTIONARIES FOR LEXEMES && TOKENS
def t_ignore(t):
    r'\n' # digit character
    t.value = int(t.value)
    return t
tokens = [
    'KEYWORD',
    'SEPARATOR',
    'IDENTIFIER',
    'OPERATIOR',
    'NUMBER'
]

# ACCEPTS .TXT FILE FOR INPUT && SCANS TEXT
def accept_file(): pass

# OUTPUT FORMAT: <lexemes> = <tokens>
def print_output(): pass
