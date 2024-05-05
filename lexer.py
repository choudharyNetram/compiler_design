import re
import os
import argparse


""" 
token_classes = [
        ('keyword', r'\b(void|assign|at|string|int|func|prnt|let|tuple|var|head|tail|list|size|agar|baki|nahito|jabtak|bool|respond|try|catch|concat|slice|replace|tue|false)\b'),
        ('identifier', r'[a-zA-Z_][a-zA-Z0-9_]*'),
        ('number', r'[1-9][0-9]*'),
        ('compareop', r'!=|==|<|>|>=|<='),
        ('binaryop', r'\+|-|\* |/|%| \b and\b|\b or\b'),
        ('unaryop', r'\+\+|--') ,
        ('semicolon', r';'),
        ('comma', r','),
        ('assign', r'='),
        ('colon', r':'),
        ('dot', r'.'),
        ('lclosep', r'\('),
        ('rclosep', r'\)'),
        ('lopenp', r'\['),
        ('ropenp', r'\])'),
        ('lcurlp', r'\{'),
        ('rcurlp', r'\}'),
        ('comment', r'\$[^\n]*|\$\*(.*?)\*\$', re.DOTALL)

    ]
"""
class Token:
    def __init__(self, token_type, value=None):
        self.token_type = token_type
        self.value = value

    def __str__(self):
        return f"Token({self.token_type}, {self.value})"

class Lexer:
    def __init__(self, input_text):
        self.input_text = input_text
        self.current_position = 0
        self.current_char = self.input_text[self.current_position]
        self.tokens = []

    # for incrementing position of current-character in input_text 
    def incrementpos(self):
        self.current_position += 1
        if self.current_position < len(self.input_text):
            self.current_char = self.input_text[self.current_position]
        else:
            self.current_char = None

    def skip_whitespace(self):
        while self.current_char is not None and self.current_char.isspace():
            self.incrementpos()

    # regular expression: [a-zA-Z_][a-zA-Z0-9_]*
    def find_identifier(self):
        result = ""
        while self.current_char is not None and (self.current_char.isalnum() or self.current_char == '_'):
            result += self.current_char
            self.incrementpos()
        return result
    
    # regular expression of numbers: [1-9][0-9]*
    def find_number(self):
        result = ""
        while self.current_char is not None and self.current_char.isdigit():
            result += self.current_char
            self.incrementpos()
        return int(result)


    def find_string(self):
        result = ""
        self.incrementpos()  # Skip the opening quote
        while self.current_char is not None and self.current_char != '"':
            result += self.current_char
            self.incrementpos()
        self.incrementpos()  # Skip the closing quote
        return result

  
    def get_next_token(self):
        while self.current_char is not None:
            if self.current_char.isspace():
                self.skip_whitespace()
                continue

            # Check for keywords
            # Begining of a identifier: must start with [a-zA-Z_]
            if self.current_char.isalpha() or self.current_char == '_':
                identifier = self.find_identifier()
                if identifier in ["assign", "true", "false" , "string", "int", "prnt", "let", "tuple", "var", "head", "tail", "list", "size", "agar", 
                                  "baki", "nahito", "jabtak", "func", "bool", "respond", "try", "throw", "catch", "at",  "void", "concat", "slice", "replace"]:
                    self.tokens.append(Token("keywords", identifier))
                elif identifier == 'and' or identifier == 'or':
                    self.tokens.append(Token("binaryop", identifier))
                   
                else:
                    self.tokens.append(Token("identifier", identifier))
            elif self.current_char.isdigit():
                number = self.find_number()
                self.tokens.append(Token("number", number))
            elif self.current_char == '"':
                self.tokens.append(Token("quote", '\"'))
                string = self.find_string()
                self.tokens.append(Token("string", string))
                self.tokens.append(Token("quote", "\""))
            elif self.current_char == '=':
                self.incrementpos()
                if self.current_char == '=':
                    self.tokens.append(Token("compareop", "=="))
                    self.incrementpos()
                else:
                    self.tokens.append(Token("assign", "="))
            elif self.current_char == ':':
                self.tokens.append(Token("colon", ":"))
                self.incrementpos()
            elif self.current_char == ';':
                self.tokens.append(Token("semicolon", ";"))
                self.incrementpos()
            elif self.current_char == '.':
                self.tokens.append(Token("dot", "."))
                self.incrementpos()
            elif self.current_char == ',':
                self.tokens.append(Token("comma", ","))
                self.incrementpos()
            elif self.current_char == '(':
                self.tokens.append(Token("lclosep", "("))
                self.incrementpos()
            elif self.current_char == ')':
                self.tokens.append(Token("rclosep", ")"))
                self.incrementpos()
            elif self.current_char == '[':
                self.tokens.append(Token("lopenp", "["))
                self.incrementpos()
            elif self.current_char == ']':
                self.tokens.append(Token("ropenp", "]"))
                self.incrementpos()
            elif self.current_char == '{':
                self.tokens.append(Token("lcurlp", "{"))
                self.incrementpos()
            elif self.current_char == '}':
                self.tokens.append(Token("rcurlp", "}"))
                self.incrementpos()
            elif self.current_char == '+':
                self.incrementpos()
                if self.current_char == '+':
                    self.tokens.append(Token("unaryop", "++"))
                    self.incrementpos()
                else:
                    self.tokens.append(Token("binaryop", "+"))

            elif self.current_char == '-':
                self.incrementpos()
                if self.current_char == '-':
                    self.tokens.append(Token("unaryop", "--"))
                    self.incrementpos()
                else:
                    self.tokens.append(Token("binaryop", "-"))
            
            

            elif self.current_char == '*':
                self.incrementpos()
                if self.current_char == '*':
                    self.tokens.append(Token("binaryop", "**"))
                    self.incrementpos()
                else:
                    self.tokens.append(Token("binaryop", "*"))
                    
            elif self.current_char == '/' or self.current_char == "%":
                self.tokens.append(Token("binaryop", self.current_char))
                self.incrementpos()
           
            elif self.current_char == '<':
                self.incrementpos()
                if self.current_char == '=':
                    self.tokens.append(Token("compareop", "<="))
                    self.incrementpos()
                else:
                    self.tokens.append(Token("compareop", "<"))               
            elif self.current_char == '>':
                self.incrementpos()
                if self.current_char == '=':
                    self.tokens.append(Token("compareop", ">="))
                    self.incrementpos()
                else:
                    self.tokens.append(Token("compareop", ">"))
            elif self.current_char == '!':
                self.incrementpos()
                if self.current_char == '=':
                    self.tokens.append(Token("compareop", "!="))
                    self.incrementpos()
                else:
                    self.tokens.append(Token("NOT", "!"))
                    
            elif self.current_char == '$':
                self.incrementpos()
                if self.current_char == '*':
                    # Multi-line comment
                    self.incrementpos()  # Skip '*'
                    while self.current_char is not None and not (self.current_char == '*' and self.input_text[self.current_position + 1] == '$'):
                        self.incrementpos()
                    self.incrementpos()  # Skip '*'
                    self.incrementpos()  # Skip '$'
                else:
                    # Single-line comment
                    while self.current_char is not None and self.current_char != '\n':
                        self.incrementpos()
            else:
                raise Exception(f"Unknown character: {self.current_char}")

        self.tokens.append(Token("EOF"))
        return self.tokens


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Lexer for programming language")
    parser.add_argument("file", type=str, help="Input file containing the source code")
    args = parser.parse_args()

    filename = os.path.join(os.path.dirname(__file__), "testcases", args.file)
    with open(filename, 'r', encoding='utf-8') as file:
        code = file.read()

    lexer = Lexer(code)
    tokens = lexer.get_next_token()
    tokensInFormat = []

    for token in tokens:
        if token.token_type == "EOF":
            break 
        tokensInFormat.append((f'<{token.token_type}, "{token.value}">'))

    print(tokensInFormat)
