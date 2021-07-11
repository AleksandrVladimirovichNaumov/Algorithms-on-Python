"""
Задание 6.
Задание на закрепление навыков работы с очередью
Реализуйте структуру "доска задач".
Структура должна предусматривать наличие несольких очередей задач, например,
1) базовой, откуда задачи берутся, решаются и отправляются в список решенных
2) очередь на доработку, когда нерешенные задачи из первой очереди отправляются
на корректировку решения
После реализации структуры, проверьте ее работу на различных сценариях
Примечание: в этом задании вспомните ваши знания по работе с ООП
и опирайтесь на пример урока
Прошу вас внимательно читать ТЗ и не забыть выполнить все пункты.
Задание творческое. Здесь нет жестких требований к выполнению.
"""


class TaskBoard:
    def __init__(self, task_type):
        self.elems = []
        self.task_type = task_type

    def is_empty(self):
        print(f'All tasks were deleted from {self.task_type}')
        self.elems.clear()

    def to_task_board(self, item):
        self.elems.insert(0, item)
        print(f'{self.elems[0]} was added to {self.task_type}')

    def from_task_board(self, to_board):
        if self.size() != 0:    # cannot move tasks from a board if there are no tasks on a board
            if to_board.task_type == self.task_type:    # cannot move tasks to current board
                print('you cannot move it to same task group')
            else:
                print(f'\n{self.elems[-1]} was removed from {self.task_type}')    # print should be before elem.pop()
                to_board.to_task_board(self.elems[-1])
                self.elems.pop()
        else:
            print(f'No available tasks in {self.task_type} to move')

    def size(self):
        return len(self.elems)


# checking class methods
if __name__ == '__main__':
    normal_tasks = TaskBoard('normal tasks')
    finished_tasks = TaskBoard('finished tasks')
    tasks_for_rework = TaskBoard('tasks to rework')

    normal_tasks.from_task_board(finished_tasks)
    print(normal_tasks.size())
    for i in range(5):
        normal_tasks.to_task_board(f'task_{i + 1}')

    normal_tasks.from_task_board(finished_tasks)
    normal_tasks.from_task_board(finished_tasks)
    normal_tasks.from_task_board(finished_tasks)
    normal_tasks.from_task_board(tasks_for_rework)
    normal_tasks.from_task_board(tasks_for_rework)
    normal_tasks.from_task_board(tasks_for_rework)
    print(f'{normal_tasks.size()} tasks in {normal_tasks.task_type}')
    tasks_for_rework.from_task_board(finished_tasks)
    tasks_for_rework.from_task_board(finished_tasks)
    tasks_for_rework.from_task_board(finished_tasks)
    print(f'{tasks_for_rework.size()} tasks in {tasks_for_rework.task_type}')
    print(f'{finished_tasks.task_type}: {finished_tasks.elems}')
    finished_tasks.is_empty()
    print(f'{finished_tasks.size()} tasks in {finished_tasks.task_type}')
    print(f'{finished_tasks.task_type}: {finished_tasks.elems}')
