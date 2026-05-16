def isValid(self, s: str) -> bool:
        parentheses = {
            "(":")",
            "{":"}",
            "[":"]",
        }
        stack = []
        for char in s:
            if char in parentheses:
                stack.append(parentheses[char])
                continue
            if not stack:
                return False
            popped = stack.pop()

            if char != popped:
                return False
        return len(stack) == 0