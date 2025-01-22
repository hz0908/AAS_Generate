def generate_task_string(task_count):
    result = ""
    for i in range(task_count + 1):
        if i == 0:
            result += f"task{i}_done = 1\n"
        else:
            result += f"task{i}_done = 0\n"
    return result


task_count = int(input("请输入 task_count: "))
print(generate_task_string(task_count))