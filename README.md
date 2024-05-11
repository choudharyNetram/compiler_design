### Token Generation
To generate tokens, run the following command:
python lexer.py sample1.ajnv


Run `python lexer.py <your_file.ajnv>`.

### Abstract Syntax Tree (AST) Generation
To generate the AST, execute the following command:

python parser_with_ast.py testcases/sample1.ajnv


### AST Visualization using anyTree
To visualize the AST using anyTree, run the command:
python semantic_analysis2.py testcases/sample1.ajnv


### WebAssembly (WAT) Code Generation
Generating the .wat File
To generate the .wat file, use the following command:
python codeGen2.py testcases/arthimetic.ajnv




