# Token Classes and Regular Expressions explanation

1. **Keyword (e.g., void, assign, string, int, ...):**
   - Regular Expression: `r'\b(void|assign|at|string|int|func|prnt|let|tuple|var|head|tail|list|size|agar|baki|nahito|jabtak|bool|respond|try|catch|concat|slice|replace|true|false)\b'`
   - Explanation: Matches any of the specified keywords as whole words and classifies it as Keyword.

2. **Identifier (e.g., variable names):**
   - Regular Expression: `r'[a-zA-Z_][a-zA-Z0-9_]*'`
   - Explanation: Matches valid identifiers, starting with a letter or underscore, followed by letters, digits, or underscores.

3. **Number (e.g., 123):**
   - Regular Expression: `r'0|[1-9][0-9]*'`
   - Explanation: Matches positive integers.

4. **Comparison Operators (e.g., ==, <, >, <=):**
   - Regular Expression: `r'!=|==|<|>|>=|<='`
   - Explanation: Matches any of the specified comparison operators.

5. **Binary Operators (e.g., +, -, *, /, and, or):***
   - Regular Expression: `r'\+|-|\* |/|%| \b and\b|\b or\b'`
   - Explanation: Matches any of the specified binary operators, including logical operators.

6. **Unary Operators (e.g., ++, --):**
   - Regular Expression: `r'\+\+|--'`
   - Explanation: Matches any of the specified unary operators.

7. **Semicolon (;):**
   - Regular Expression: `r';'`
   - Explanation: Matches the semicolon character, signifies end of statement.

8. **Comma (,):**
   - Regular Expression: `r','`
   - Explanation: Matches the comma character.

9. **Assignment Operator (=):**
   - Regular Expression: `r'='`
   - Explanation: Matches the assignment operator.

10. **Colon (:):**
    - Regular Expression: `r':'`
    - Explanation: Matches the colon character.

11. **Dot (.):**
    - Regular Expression: `r'\.'`
    - Explanation: Matches the dot character.

12. **Left Parenthesis (():**
    - Regular Expression: `r'\('`
    - Explanation: Matches the left parenthesis character.

13. **Right Parenthesis ())):**
    - Regular Expression: `r'\)'`
    - Explanation: Matches the right parenthesis character.

14. **Left Square Bracket ([):**
    - Regular Expression: `r'\['`
    - Explanation: Matches the left square bracket character.

15. **Right Square Bracket (]):**
    - Regular Expression: `r'\]'`
    - Explanation: Matches the right square bracket character.

16. **Left Curly Brace ({):**
    - Regular Expression: `r'\{'`
    - Explanation: Matches the left curly brace character.

17. **Right Curly Brace (}):**
    - Regular Expression: `r'\}'`
    - Explanation: Matches the right curly brace character.

18. **Comment (Single-line or Multi-line):**
    - Regular Expression: `r'\$[^\n]*|\$\*(.*?)\*\$'` with `re.DOTALL` flag
    - Explanation: Matches either a single-line comment (starting with `$`) or a multi-line comment (starting with `$*` and ending with `*`). The `re.DOTALL` flag allows the dot (`.`) in the regex to match newline characters as well.
