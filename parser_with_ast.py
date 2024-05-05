from lark import Lark
import sys 
grammar = """
start: program
program: statement+

statement: assignment | print_statement | variable_declaration |  if_else_statement | while_loop | closure_definition |  function_definition | unary_operation_assign | exception_handling_statement | function_call_statement | tuple_statement | array_declaration | array_operation_stms| string_ops_stms | respond_stms 
COMMENT_MULTI: /\$\*.*?\*\$/s
COMMENT: /\$.*/ 

NUMBER: /[0-9]+/

identifier:/[a-zA-Z_][a-zA-Z0-9_]*/
compareop :  EQEQ | NOTEQ | LTEQ |GTEQ |GT | LT
binaryop : PLUS | MINUS| MUL| INT_DIV| MODULO| AND| OR| POWER
PLUS  : "+" 
MINUS : "-" 
MUL   : "*"
INT_DIV : "/"
EQEQ  : "=="
NOTEQ  :"!="
GT    : ">"
LT    : "<"
GTEQ  : ">="
LTEQ  : "<="
MODULO: "%"
AND   : "and"
OR     :"or"
POWER  :"**"
boolean: TRUE | FALSE
TRUE: "true"
FALSE: "false"
unaryop : PLPL | MIMI
PLPL: "++"
MIMI: "--"

string:/"[^"]*"/

variable_type: "int" | "bool" | "string" | "void"

variable_declaration: "assign"  variable_type ":" identifier is_value ";"

is_value: "=" expression  

assignment: identifier "=" expression ";"
print_statement: "prnt" "(" expression ")" ";"

expression:  identifier | NUMBER | boolean |  string  | unary_operation| binary_operation | compare_operation | function_call | tuple_operations | array_operation | string_ops
unary_operation : expression unaryop
binary_operation : expression binaryop expression 
unary_operation_assign :  expression unaryop ";"
compare_operation : expression compareop expression

if_else_statement : "agar"  expression "{" program "}" | "agar"  expression "{" program "}" baki_s | "agar"  expression "{" program "}" nahi_to_s
baki_s : ("baki" expression "{" program baki_s)+ | ("baki" expression "{" program baki_s)+ nahi_to_s 
nahi_to_s : "nahito"  "{" program "}" 

while_loop: "jabtak" expression "{" program "}" 

function_definition : "func"  ":"  variable_type identifier "(" ")" "{"  program  "}" | "func"  ":"  variable_type identifier "(" parameter_list ")" "{" program  "}" 
parameter_list : parameter | parameter next_para 
next_para :  ("," parameter)+

parameter :  variable_type ":" identifier 

function_call : identifier "(" ")"  | identifier "(" argument_values ")"
argument_values : expression | expression next_expression 
next_expression : ("," expression)+ 

function_call_statement : identifier "(" ")"  ";" | identifier "(" argument_values ")" ";"
respond_stms :  "respond"  expression ";"

closure_definition  :  "func" ":"  variable_type identifier "(" parameter_list ")" "{" program  "func"  ":"  variable_type identifier "(" parameter_list ")" "{"  program      "}" program  "}"

exception_handling_statement : "try" "{" program "throw"  identifier ";" "}"  "catch"  "(" identifier ")" "{" program "}"

tuple_statement : "let"  "tuple" ":" identifier "=" "("  argument_values ")" ";"
tuple_operations : identifier "." "at" "(" expression ")"  


array_declaration : "assign"  variable_type ":" identifier "("  expression  ")" ";"| "assign"  variable_type ":" identifier "("  expression  ")" "=" "[" argument_values "]" ";"

array_operation : identifier "." ("size" | "head" | "tail") "(" ")"   |  identifier "[" expression "]"  


array_operation_stms : identifier "[" expression "]" "="  expression ";"

slice : "slice"
concat : "concat"
string_ops : identifier "." slice "(" expression "," expression ")" | identifier "." concat "(" identifier ")" 
string_ops_stms : identifier "." slice "(" expression "," expression ")" ";" | identifier "." concat "(" identifier ")" ";"

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

# Display the  AST
print("AST:\n", tree.pretty())