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