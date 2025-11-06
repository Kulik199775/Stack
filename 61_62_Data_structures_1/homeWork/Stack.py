class Node:
    """
    Узел для односвязного списка.

    Attributes:
        data: Данные, хранящиеся в узле
        next_node: Ссылка на следующий узел в списке
    """

    def __init__(self, data, next_node=None):
        """
        Инициализирует узел.

        Args:
            data: Данные для хранения в узле
            next_node: Следующий узел в списке (по умолчанию None)
        """
        self.data = data
        self.next_node = next_node


class Stack:
    """
    Реализация стека на основе односвязного списка.

    Attributes:
        stack_size (int): Максимальный размер стека
        top (Node): Верхний элемент стека
    """

    def __init__(self, stack_size=5, top=None):
        """
        Инициализирует стек.

        Args:
            stack_size (int): Максимальный размер стека (по умолчанию 5)
            top (Node): Начальный верхний элемент стека (по умолчанию None)
        """
        self.stack_size = stack_size
        self.top = top  # через топ обращаемся к атрибутам ноды

    def push(self, data):
        """
        Добавляет элемент на вершину стека.

        Args:
            data: Данные для добавления в стек

        Returns:
            str: Сообщение об ошибке если стек переполнен, иначе None
        """
        if self.size_stack() < self.stack_size:
            new_node = Node(data)
            new_node.next_node = self.top  # та вершина которая была
            self.top = new_node  # переназначаем вершину
        else:
            print("Стэк переполнен")
            return "Стэк переполнен"

    def pop(self):
        """
        Удаляет и возвращает элемент с вершины стека.

        Returns:
            Данные удаленного элемента или сообщение "Стэк пуст"
        """
        if self.top:
            remove_last = self.top
            self.top = self.top.next_node
            return remove_last.data
        else:
            return "Стэк пуст"

    def is_empty(self):
        """
        Проверяет, пуст ли стек.

        Returns:
            bool: True если стек пуст, иначе False
        """
        if self.top:
            return False
        else:
            return True

    def is_full(self):
        """
        Проверяет, заполнен ли стек.

        Returns:
            bool: True если стек заполнен, иначе False
        """
        if self.stack_size == self.size_stack():
            return True
        else:
            return False

    def clear_stack(self):
        """Очищает стек, удаляя все элементы."""
        while self.top:
            self.pop()

    def get_data(self, index):
        """
        Возвращает данные элемента по указанному индексу.

        Args:
            index (int): Индекс элемента (0 - вершина стека)

        Returns:
            Данные элемента или сообщение "Out of range"
        """
        counter = 0
        stack_item = self.top
        while stack_item:
            if counter == index:
                return stack_item.data
            stack_item = stack_item.next_node
            counter += 1
        return f"Out of range"

    def size_stack(self):
        """
        Возвращает текущий размер стека.

        Returns:
            int: Количество элементов в стеке
        """
        counter = 0
        stack_item = self.top
        while stack_item:
            counter += 1
            stack_item = stack_item.next_node
        return counter

    def counter_int(self):
        """
        Подсчитывает количество целых чисел в стеке.

        Returns:
            int: Количество целых чисел в стеке
        """
        counter = 0
        stack_item = self.top
        while stack_item:
            if isinstance(stack_item.data, int):
                counter += 1
            stack_item = stack_item.next_node
        return counter


stack = Stack()
stack.push(1)
stack.push("sta")
stack.push(2)
stack.push(2.5)
stack.push("sta")
print(stack.counter_int())
