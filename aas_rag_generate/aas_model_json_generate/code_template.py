def insert_segments(import_seg, init_seg, reset_seg, num_tasks, task_segs):
    code_template = '''from isaacsim import SimulationApp

simulation_app = SimulationApp("headless": False)



{import_seg}


my_world = World(stage_units_in_meters=1.0)
my_world.scene.add_default_ground_plane()


{init_seg}


my_world.reset()


task0_done = 1
task1_done = 0
task2_done = 0
task3_done = 0

reset_needed = False
while simulation_app.is_running():
    my_world.step(render=True)
    if my_world.is_stopped() and not reset_needed:
        reset_needed = True
    if my_world.is_playing():
        if reset_needed:
            {reset_seg}

        if task0_done :
            {task0_seg}

        if task1_done :
            {task1_seg}

        if task2_done :
            {task2_seg}

        if task3_done :
            print("job done")
            


simulation_app.close()'''
    # 检查任务数量和任务段的数量是否匹配
    if len(task_segs)!= num_tasks:
        raise ValueError("The number of task segments does not match the number of tasks specified.")
    # 替换任务段
    task_seg_dict = {}
    for i in range(num_tasks):
        task_seg_dict[f"task{i}_seg"] = task_segs[i] if i < len(task_segs) else ""
    # 填充模板
    final_code = code_template.format(import_seg=import_seg, init_seg=init_seg, reset_seg=reset_seg, **task_seg_dict)
    return final_code


# 示例调用
import_seg = "# import seg"
init_seg = "# init seg"
reset_seg = "# reset seg"
num_tasks = 4
task_segs = ["# task1 seg", "# task2 seg", "# task3 seg"]
final_code = insert_segments(import_seg, init_seg, reset_seg, num_tasks, task_segs)
print(final_code)