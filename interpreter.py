import sys
from parser import BipError


class Interpreter:
    def __init__(self, tokens, jumps):
        self.tokens = tokens
        self.jumps = jumps
        self.tape = [0]
        self.ptr = 0

    def read_number(self, line):
        try:
            raw = input("sayı ver: ")
        except EOFError:
            return 0
        try:
            return int(raw) % 256
        except ValueError:
            raise BipError(f"satır {line}: '{raw}' sayı değil ki")

    def run(self):
        pc = 0
        while pc < len(self.tokens):
            tok = self.tokens[pc]
            kind = tok.kind

            if kind == "INC":
                # 255'ten sonra 0'a sarıyor, araba kilometresi gibi
                self.tape[self.ptr] = (self.tape[self.ptr] + 1) % 256
            elif kind == "DEC":
                self.tape[self.ptr] = (self.tape[self.ptr] - 1) % 256
            elif kind == "RIGHT":
                self.ptr += 1
                if self.ptr == len(self.tape):
                    self.tape.append(0)
            elif kind == "LEFT":
                if self.ptr == 0:
                    raise BipError(f"satır {tok.line}: en soldasın, daha sola gidemezsin")
                self.ptr -= 1
            elif kind == "PRINT_CHAR":
                sys.stdout.write(chr(self.tape[self.ptr]))
            elif kind == "PRINT_NUM":
                sys.stdout.write(str(self.tape[self.ptr]))
            elif kind == "INPUT":
                sys.stdout.flush()
                self.tape[self.ptr] = self.read_number(tok.line)
            elif kind == "LOOP_START":
                # hücre 0 ise döngüye hiç girme
                if self.tape[self.ptr] == 0:
                    pc = self.jumps[pc]
            elif kind == "LOOP_END":
                # döngü bitmediyse başa sar
                if self.tape[self.ptr] != 0:
                    pc = self.jumps[pc]

            pc += 1
        sys.stdout.flush()
