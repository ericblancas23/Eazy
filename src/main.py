import lexer

def main():
    content = ""
    with open('test.lang', 'r') as file:
        content = file.read()
    print(content)

    lex = lexer.Lexer(content)
    tokens = lex.tokenize()
main()