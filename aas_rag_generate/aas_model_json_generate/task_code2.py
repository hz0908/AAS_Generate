def generate_task_string(task_code_list):
    result = ""
    index = 0
    for code in task_code_list:
        task_done_key = f"task{index}_done"
        result += f"if {task_done_key}:\n    {code}\n"
        index += 1
    if index > 0:
        last_task_done_key = f"task{index - 1}_done"
        result += f"if {last_task_done_key}:\n    print(\"job done\")"
    return result

#示例 task_code_list
task_code_list = [
    "print('Task 0 is completed')",
    "print('Task 1 is completed')",
    "print('Task 2 is completed')",
    "print('Task 3 is completed')"
]
print(generate_task_string(task_code_list))