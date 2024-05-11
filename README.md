### Token Generation
To generate tokens, run the following command:
```bash
python lexer.py sample1.ajnv



Abstract Syntax Tree (AST) Generation
To generate the AST, execute the following command:

python parser_with_ast.py testcases/sample1.ajnv


AST Visualization using anyTree
To visualize the AST using anyTree, run the command:
python semantic_analysis2.py testcases/sample1.ajnv


WebAssembly (WASM) Code Generation
Generating the .wat File
To generate the .wat file, use the following command:
python codeGen2.py testcases/arthimetic.ajnv




### For generating the Tokens: python lexer.py sample1.ajnv

### For generating the AST: python parser_with_ast.py testcases/sample1.ajnv

### AST with anyTree: python semantic_analysis2.py testcases/sample1.ajnv



### For Generating the WASM code: 
1. command for generating the wat file:
   $ python codeGen2.py testcases/arthimetic.ajnv
