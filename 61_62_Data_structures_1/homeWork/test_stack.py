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

    def test_clear_stack(self):
        """Тест очистки стека"""
        stack = Stack()
        stack.push(1)
        stack.push(2)
        stack.clear_stack()
        assert stack.is_empty() is True
        assert stack.top is None

    def test_get_data(self):
        """Тест получения данных по индексу"""
        stack = Stack()
        stack.push(1)
        stack.push(2)
        stack.push(3)
        assert stack.get_data(0) == 3 #Вершина
        assert stack.get_data(1) == 2
        assert stack.get_data(2) == 1

    def test_get_data_out_of_range(self):
        """Тест получения данных по несуществующему индексу"""
        stack = Stack()
        stack.push(1)
        assert stack.get_data(5) == 'Out of range'

    def test_size_stack(self):
        """Тест получения размера стека"""
        stack = Stack()
        assert stack.size_stack() == 0
        stack.push(1)
        assert stack.size_stack() == 1
        stack.push(2)
        assert stack.size_stack() == 2

    def test_counter_int(self):
        """Тест подсчета целых чисел в стеке"""
        stack = Stack()
        stack.push(1)
        stack.push('string')
        stack.push(2.5)
        stack.push(3)
        stack.push([1, 2, 3])
        assert stack.counter_int() == 2

    def test_counter_int_no_integer(self):
        """Тест подсчета целых чисел когда их нет в стеке"""
        stack = Stack()
        stack.push('string')
        stack.push(2.5)
        stack.push([1, 2, 3])
        assert stack.counter_int() == 0

    def test_lifo_behavior(self):
        """Тест поведения LIFO"""
        stack = Stack(stack_size=3)
        stack.push(1)
        stack.push(2)
        stack.push(3)
        assert stack.pop() == 3
        assert stack.pop() == 2
        assert stack.pop() == 1
        assert stack.is_empty() is True

if __name__ == '__main__':
    pytest.main([__file__, '-v'])

