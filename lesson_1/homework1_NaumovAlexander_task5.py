"""
Задание 5.
Задание на закрепление навыков работы со стеком
Реализуйте структуру "стопка тарелок".
Мы можем складывать тарелки в стопку и при превышении некоторого значения
нужно начать складывать тарелки в новую стопку.
Структура должна предусматривать наличие нескольких стеков.
Создание нового стека происходит при достижении предыдущим стеком порогового значения.
Реализуйте по аналогии с примером, рассмотренным на уроке, необходимые методы,
для реализации это структуры, добавьте новые методы (не рассмотренные в примере с урока)
для реализации этой задачи.
После реализации структуры, проверьте ее работу на различных сценариях
Подсказка:
Отдельне стопки можно реализовать через:
1) созд-е экземпляров стека (если стопка - класс)
или
2) lst = [[], [], [], [],....]
Примечание: в этом задании вспомните ваши знания по работе с ООП
и опирайтесь на пример урока
Прошу вас внимательно читать ТЗ и не забыть выполнить все пункты.
Задание творческое. Здесь нет жестких требований к выполнению.
"""


class PlatesStack:
    # list which keep all stacks names
    list_of_stacks_names = []
    # list which keep all stacks
    list_of_stacks = []

    def __init__(self, stack_name, max_quantity):
        self.elems = []  # list for keeping 'plates'
        self.stack_name = stack_name
        self.max_quantity = max_quantity  # stack size
        PlatesStack.list_of_stacks.append(self)  # adding stack to list of stacks
        PlatesStack.list_of_stacks_names.append(self.stack_name)  # adding stack's name to list of stacks names

    def is_empty(self):
        return self.elems == []

    @classmethod
    def create_new_stack(cls, name, stack_size):
        """
        creating new class object. Used in push_in() method when stack is full.
        :param name: name of a new stuck
        :param stack_size: size of new stack
        :return: - (creates new class obj)
        """
        cls(name, stack_size)

    def push_in(self, el):
        if len(self.elems) == self.max_quantity:
            try:  # if inputted data is not suitable
                name = input(f'Current stack is full. Please enter name of a new stack'
                             f' (already exist{PlatesStack.list_of_stacks_names}): ')
                stack_size = int(input('Please enter new stack size (integer > 0): '))
                self.create_new_stack(name, stack_size)
                print(
                    f'New stack "{name}" was created. Please use it to add plates.'
                    f' Available stacks are: {PlatesStack.list_of_stacks_names}')
            except Exception as e:
                print(f"Error: {e}.")
        else:
            self.elems.append(el)

    @staticmethod
    def get_list_of_plates_stack():
        return PlatesStack.list_of_stacks

    @staticmethod
    def get_list_of_plates_stack_names():
        return PlatesStack.list_of_stacks_names

    def pop_out(self):
        return self.elems.pop()

    def get_val(self):
        return self.elems

    def stack_current_size(self):
        return len(self.elems)

    def stack_max_size(self):
        return self.max_quantity

    def get_name(self):
        return self.stack_name


# creating stack
stack_1 = PlatesStack('stack_1', 10)

# overloading stack
for i in range(11):
    print(f'{stack_1.stack_name}: {stack_1.stack_current_size()} of {stack_1.stack_max_size()} '
          f'with values {stack_1.get_val()}')
    stack_1.push_in(f'plate_{i + 1}')

# checking that PlatesStack objects created
print(f'current stacks are: {PlatesStack.list_of_stacks}.')


