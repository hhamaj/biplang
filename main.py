import os
import sys
from lexer import Lexer
from parser import Parser, BipError
from interpreter import Interpreter


def main():
    if len(sys.argv) < 2:
        print("usage: bip <filename>.bip")
        exit(1)

    filepath = sys.argv[1]
    filename, extention = os.path.splitext(os.path.basename(filepath))

    if not os.path.isfile(filepath):
        print("idk this guy:", filepath)
        exit(1)

    if extention != ".bip":
        print("we only work with .bip files and not", extention)
        exit(1)

    with open(filepath, encoding="utf-8") as f:
        text = f.read()

    try:
        tokens = Lexer(text).tokenize()
        tokens, jumps = Parser(tokens).parse()
        Interpreter(tokens, jumps).run()
    except BipError as e:
        print("\nkaboom! hata:", e)
        exit(1)


if __name__ == "__main__":
    main()
