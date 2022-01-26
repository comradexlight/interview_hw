class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return self.stack == []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack[len(self.stack) - 1]

    def size(self):
        return len(self.stack)


def matches(open_, close):
    opens = "([{"
    closers = ")]}"
    return opens.index(open_) == closers.index(close)


def balance_checker(text):
    s = Stack()
    balanced = True
    index = 0
    while index < len(text) and balanced:
        symbol = text[index]
        if symbol in "([{":
            s.push(symbol)
        else:
            if s.is_empty():
                balanced = False
            else:
                top = s.pop()
                if not matches(top, symbol):
                    balanced = False
        index = index + 1
    if balanced and s.is_empty():
        return 'Сбалансированно'
    else:
        return 'Несбалансированно'


if __name__ == '__main__':
    print(balance_checker('(((([{}]))))'))
    print(balance_checker('[([])((([[[]]])))]{()}'))
    print(balance_checker('{{[()]}}'))
    print(balance_checker('}{}'))
    print(balance_checker('{{[(])]}}'))
    print(balance_checker('[[{())}]'))
