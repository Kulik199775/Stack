import pytest


class TestNode:
    """Тесты для класса Node."""

    def test_node_creation(self):
        """Тест создания узла с данными."""
        node = Node(10)
        assert node.data == 10
        assert node.next_node is None

    def test_node_with_next(self):
        """Тест создания узла со ссылкой на следующий узел."""
        next_node = Node(20)
        node = Node(10, next_node)
        assert node.data == 10
        assert node.next_node == next_node

class TestStack:
    """Тесты для класса Stack."""

    def test_stack_creation(self):
        """Тест создания стека с параметрами по умолчанию."""
        stack = Stack()
        assert stack.stack_size == 5
        assert stack.top is None
        assert stack.is_empty() is True

    def test_stack_creation_custom_size(self):
        """Тест создания стека с пользовательским размером."""
        stack = Stack(stack_size=10)
        assert stack.stack_size == 10
        assert stack.top is None

    def test_push(self):
        """Тест добавления элемента в стек."""
        stack = Stack()
        stack.push(1)
        assert stack.top.data == 1
        assert stack.size_stack() == 1

    def test_push_multiple(self):
        """Тест добавления нескольких элементов в стек."""
        stack = Stack(stack_size=3)
        stack.push(1)
        stack.push(2)
        stack.push(3)
        assert stack.top.data == 3
        assert stack.size_stack() == 3

    def test_push_full_stack(self):
        """Тест добавления в заполненный стек."""
        stack = Stack(stack_size=2)
        stack.push(1)
        stack.push(2)
        result = stack.push(3)  # Попытка добавить в заполненный стек
        assert result == "Стэк переполнен"
        assert stack.size_stack() == 2

    def test_pop(self):
        """ Тест извлечения элемента из стека"""
        stack = Stack()
        stack.push(1)
        stack.push(2)
        assert stack.pop() == 2
        assert stack.pop() == 1

    def test_pop_empty(self):
        """Тест извлечения из пустого стека."""
        stack = Stack()
        result = stack.pop()
        assert result == 'Стек пуст'

    def test_is_empty(self):
        """Тест проверки пустого стека"""
        stack = Stack()
        assert stack.is_empty() is True
        stack.push(1)
        assert stack.is_empty() is False

    def test_is_full(self):
        stack = Stack(stack_size=2)
        assert stack.is_full() is False
        stack.push(1)
        assert stack.is_full() is False
        stack.push(2)
        assert stack.is_full() is True
