def insert_segments(import_str, init_str, task_flag_str, reset_str, task_str):
    code_template = '''
#import 
{import_str}

my_world = World(stage_units_in_meters=1.0)
my_world.scene.add_default_ground_plane()

#init 
{init_str}

my_world.reset()

#task flag 
{task_flag_str}

reset_needed = False
while simulation_app.is_running():
    my_world.step(render=True)
    if my_world.is_stopped() and not reset_needed:
        reset_needed = True
    if my_world.is_playing():
        if reset_needed:
            #reset 
            {reset_str}
            
        #task 
        {task_str}
simulation_app.close()
'''
    final_code = code_template.format(
        import_str=import_str,
        init_str=init_str,
        task_flag_str=task_flag_str,
        reset_str=reset_str,
        task_str=task_str
    )

    code_head = '''
from isaacsim import SimulationApp

simulation_app = SimulationApp({"headless": False})

'''
    return code_head+final_code


# 示例调用
import_str = "导入所需的模块"
init_str = "初始化相关代码"
task_flag_str = "任务标志相关代码"
reset_str = "重置相关代码"
task_str = "具体任务相关代码"
final_code = insert_segments(import_str, init_str, task_flag_str, reset_str, task_str)
print(final_code)