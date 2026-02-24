new_tasks = ['task_001', 'task_011', 'task_007', 'task_015', 'task_005']
completed_tasks = ['task_002', 'task_012', 'task_006']

# 1. Перенести task_005 из new_tasks в completed_tasks (в одно действие)
completed_tasks.append(new_tasks.pop(new_tasks.index('task_005')))

# 2. Удалить task_007 из new_tasks
new_tasks.remove('task_007')

# 3. Вывести последнюю задачу из new_tasks (повышенный приоритет)
print(new_tasks[-1])