"""
Задание 1.
Реализуйте кодирование строки "по Хаффману".
У вас два пути:
1) тема идет тяжело? тогда вы можете, опираясь на пример с урока, сделать свою!!! версию алгоритма
Разрешается и приветствуется изменение имен переменных, выбор других коллекций, различные изменения
и оптимизации.
2) тема понятна? постарайтесь сделать свою реализацию.
Вы можете реализовать задачу, например, через ООП или предложить иной подход к решению.
"""

# Решение через ООП
from collections import Counter, deque


class HuffmanCode:

    def __init__(self, string_value):
        self.string_value = string_value
        self.sorted_dict = deque(sorted(Counter(string_value).items(), key=lambda item: item[1]))
        self.tree = self.get_tree()
        self.code_table = dict()
        self.get_code(self.tree)

    def get_tree(self):
        tree_dict = dict()
        deque_obj = self.sorted_dict.copy()
        while len(deque_obj) > 1:
            tree_dict[0] = deque_obj[0][0]
            tree_dict[1] = deque_obj[1][0]
            weight = deque_obj[0][1] + deque_obj[1][1]
            for i, _count in enumerate(deque_obj):
                if weight > _count[1]:
                    continue
                else:
                    deque_obj.insert(i, (tree_dict, weight))
                    break
            else:
                deque_obj.append((tree_dict, weight))
            deque_obj.popleft()
            deque_obj.popleft()
            tree_dict = dict()
        return deque_obj[0][0]

    def get_code(self, tree, path=''):
        if not isinstance(tree, dict):
            self.code_table[tree] = path
        else:
            self.get_code(tree[0], path=f'{path}0')
            self.get_code(tree[1], path=f'{path}1')

    def get_string_code(self):
        # почему-то при использовании list comprehension у меня скрипт уходит в луп
        # result_code = [i for i in self.string_value]
        # result_code = ''.join(result_code)
        result_code = ''
        for i in self.string_value:
            result_code += self.code_table[i]
        return result_code

    def decoding(self, code_string):
        res = ''
        i = 0
        codes_dict = self.code_table
        while i < len(code_string):
            for code in codes_dict:
                if code_string[i:].find(codes_dict[code]) == 0:
                    res += code
                    i += len(codes_dict[code])
        return res


huffman_obj1 = HuffmanCode('beep boop beer!')
print(f"Исходная строка:\n'{huffman_obj1.string_value}'")
print(f"Дерево:\n{huffman_obj1.tree}")
print(f"Таблица c кодами:\n{huffman_obj1.code_table}")
print(f"Строка кода после кодирования:\n{huffman_obj1.get_string_code()}")
print(f"Декодированная строка:\n'{huffman_obj1.decoding(huffman_obj1.get_string_code())}'")

