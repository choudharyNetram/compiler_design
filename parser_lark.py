from lark import Token, Lark
import re
import sys 
grammar = """
start: program
program: statement+


statement: assignment | print_statement | variable_declaration |  if_else_statement | while_loop | closure_definition | function_definition | unary_operation_assign | exception_handling_statement | function_call_statement | tuple_statement | array_declaration | array_operation_stms| string_ops_stms | respond_stms 
COMMENT_MULTI: /\$\*.*?\*\$/s
COMMENT: /\$.*/ 

NUMBER: /[0-9]+/

identifier:/[a-zA-Z_][a-zA-Z0-9_]*/
ASSIGN : "assign" 
compareop :  "==" | "<=" | "<" | ">=" | ">" | "!="
colon : ":"

semicolon : ";"
dot : "."
comma :  ","
lclosep :  "("
rclosep:  ")"
lopenp :  "["
ropenp :  "]"
lcurlp : "{"
rcurlp : "}" 
unaryop : "++" | "--"
binaryop : "+" | "-" | "**" | "*" | "/" | "%"
ASSIGN_OPT: "="


boolean: "true" | "false"
PRINT : "prnt"
quote : /"/

string:  (identifier | NUMBER)+ 
variable_type: "int" | "bool" | "string" | "void"

variable_declaration: ASSIGN variable_type colon identifier is_value semicolon

is_value: ASSIGN_OPT expression  

assignment: identifier ASSIGN_OPT expression semicolon
print_statement: PRINT lclosep expression rclosep semicolon

expression:  identifier | NUMBER | boolean | quote string quote | unary_operation| binary_operation | compare_operation | function_call | tuple_operations | array_operation | string_ops
unary_operation : expression unaryop 
binary_operation : expression binaryop expression 
unary_operation_assign :  expression unaryop semicolon 
compare_operation : expression compareop expression

agar : "agar" 
baki : "baki" 
nahito : "nahito" 
if_else_statement : agar expression lcurlp program rcurlp | agar expression lcurlp program rcurlp baki_s | agar expression lcurlp program rcurlp nahi_to_s
baki_s : (baki expression lcurlp program baki_s)+ | (baki expression lcurlp program baki_s)+ nahi_to_s 
nahi_to_s : nahito lcurlp program rcurlp 

jabtak : "jabtak"
while_loop: jabtak expression lcurlp program rcurlp 

func: "func" 
respond : "respond" 
function_definition : func colon  variable_type identifier lclosep rclosep lcurlp program  respond expression semicolon rcurlp | func colon  variable_type identifier lclosep parameter_list rclosep lcurlp program  respond expression semicolon rcurlp |  func colon  variable_type identifier lclosep parameter_list rclosep lcurlp program rcurlp
parameter_list : parameter | parameter next_para 
next_para :  (comma parameter)+
parameter :  variable_type colon identifier 

function_call : identifier lclosep rclosep  | identifier lclosep argument_values rclosep 
argument_values : expression | expression next_expression 
next_expression : (comma expression)+ 
function_call_statement : identifier lclosep rclosep  semicolon | identifier lclosep argument_values rclosep semicolon
respond_stms : respond expression semicolon

closure_definition  :  func colon  variable_type identifier lclosep parameter_list rclosep lcurlp program func colon  variable_type identifier lclosep parameter_list rclosep lcurlp program  respond expression semicolon rcurlp program respond expression semicolon rcurlp

try : "try"
throw : "throw" 
catch : "catch" 
exception_handling_statement : try lcurlp program throw identifier semicolon rcurlp catch lclosep identifier rclosep lcurlp program rcurlp

let : "let" 
tuple : "tuple" 
at : "at" 
tuple_statement : let tuple colon identifier ASSIGN_OPT lclosep  argument_values rclosep semicolon 
tuple_operations : identifier dot at lclosep expression rclosep  


array_declaration : ASSIGN variable_type colon identifier lclosep  expression  rclosep semicolon| ASSIGN variable_type colon identifier lclosep  expression  rclosep ASSIGN_OPT lopenp argument_values ropenp semicolon 

head : "head" 
tail : "tail" 
size : "size" 
array_operation : identifier dot (size | head | tail) lclosep rclosep   |  identifier lopenp expression ropenp  


array_operation_stms : identifier lopenp expression ropenp ASSIGN_OPT  expression semicolon 

slice : "slice" 
concat : "concat" 
string_ops : identifier dot slice lclosep expression comma expression rclosep | identifier dot concat lclosep identifier rclosep 
string_ops_stms : identifier dot slice lclosep expression comma expression rclosep semicolon | identifier dot concat lclosep identifier rclosep semicolon


%import common.LETTER
%import common.DIGIT
%import common.SPECIAL_CHARACTER
%import common.WS
%ignore WS
%ignore COMMENT
%ignore COMMENT_MULTI
"""

# Load the code from a file
if len(sys.argv) != 2:
    print("Run by terminal, give the path of sample's files python, path like testcases/sample1.ajnv")
    sys.exit(1)

file_path = sys.argv[1]

# Load the code from a file
with open(file_path, 'r') as file:
    code = file.read()
""" 
file_path = 'testcases/sample1.ajnv'  # Update with your file path
with open(file_path, 'r') as file:
    code = file.read()
"""
# Create the Lark parser
parser = Lark(grammar, start="start", parser='lalr')

# Parse the code
tree = parser.parse(code)

# Display the parsed tree
print("Parsed tree:\n", tree.pretty())


# custom_lexer_instance.set_input(code)
# tokens = custom_lexer_instance.get_next_token()
"""
tokens = parser.lex(code)
tokenized_code = ""

for token in tokens:
    tokenized_code += str(token) + " "

print("Tokenized code:", tokenized_code) """


# firstly trying to check the grammar using in-built lexer, once done we can modify it to use the tokens from our custom made lexer
class Token:
    def __init__(self, token_type, value=None):
        self.token_type = token_type
        self.value = value
    def __str__(self):
        return f"Token({self.token_type}, {self.value})"

class CustomLexer:
    def __init__(self):
        self.current_position = 0
        self.current_char = None
        self.tokens = []
    def set_input(self, input_text):
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
