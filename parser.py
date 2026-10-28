class BipError(Exception):
    pass


class Parser:
    def __init__(self, tokens):
        self.tokens = tokens

    def parse(self):
        # döngü başlarıyla sonlarını eşleştiriyoruz, interpreter direkt atlasın diye
        jumps = {}
        stack = []
        for i, tok in enumerate(self.tokens):
            if tok.kind == "LOOP_START":
                stack.append(i)
            elif tok.kind == "LOOP_END":
                if not stack:
                    raise BipError(f"satır {tok.line}: kapanan bir kaboom kaboom var ama açan kaboom yok")
                start = stack.pop()
                jumps[start] = i
                jumps[i] = start

        if stack:
            line = self.tokens[stack[-1]].line
            raise BipError(f"satır {line}: kaboom açıldı ama hiç kapanmadı")

        return self.tokens, jumps
