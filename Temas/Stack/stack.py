from typing import Any, Optional

class Stack:
    def __init__(self):
        self.__elements = []

    def push(self, value: Any) -> None:
        self.__elements.append(value)

    def pop(self) -> Optional[Any]:
        return self.__elements.pop() if self.__elements else None

    def size(self) -> int:
        return len(self.__elements)

    def on_top(self) -> Optional[Any]:
        return self.__elements[-1] if self.__elements else None

    def is_empty(self) -> bool:
        return len(self.__elements) == 0

    def show(self):
        aux_stack = Stack()
        while not self.is_empty():
            value = self.pop()
            print(value)
            aux_stack.push(value)
        while not aux_stack.is_empty():
            self.push(aux_stack.pop())
