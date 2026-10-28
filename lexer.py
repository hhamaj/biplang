import re

# uzun kalıplar önce gelsin, yoksa "bip bip kaboom" iki bip olarak kaçar
PATTERNS = [
    (("bip", "bip", "kaboom"), "INPUT"),
    (("kaboom", "kaboom"), "LOOP_END"),
    (("boom", "boom"), "PRINT_NUM"),
    (("bum", "bum"), "LEFT"),
    (("bip",), "INC"),
    (("dut",), "DEC"),
    (("bum",), "RIGHT"),
    (("boom",), "PRINT_CHAR"),
    (("kaboom",), "LOOP_START"),
]

KEYWORDS = {"bip", "dut", "boom", "kaboom", "bum"}


class Token:
    def __init__(self, kind, line):
        self.kind = kind
        self.line = line

    def __repr__(self):
        return f"{self.kind}@{self.line}"


class Lexer:
    def __init__(self, text):
        self.text = text

    def tokenize(self):
        tokens = []
        for line_no, line in enumerate(self.text.splitlines(), start=1):
            # bizim kelimeler dışındaki her şey yorum sayılır, at gitsin
            words = [w for w in re.findall(r"\w+", line.lower()) if w in KEYWORDS]

            # kalıplar sadece aynı satırda geçerli
            i = 0
            while i < len(words):
                for pattern, kind in PATTERNS:
                    if tuple(words[i:i + len(pattern)]) == pattern:
                        tokens.append(Token(kind, line_no))
                        i += len(pattern)
                        break
        return tokens
