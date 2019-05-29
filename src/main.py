def main():
    content = ""
    with open('test.lang', 'r') as file:
        content = file.read()
    print(content)

main()