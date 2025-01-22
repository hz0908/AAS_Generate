from prompt_info import PromptInfo
# 为每个参数定义单独的变量
system_description = "你是一个高级的python工程师，能够对用户提供的导入各pyhton库的代码进行分析，去除一些重复的库导入代码，输出最终的去重后的代码"
que1 = '''
from omni.isaac.franka import Franka
from omni.isaac.core import World
from omni.isaac.core.objects import DynamicCuboid
from omni.isaac.franka.controllers import PickPlaceController 
import numpy as np
import numpy as np
from omni.isaac.universal_robots import UR10
from omni.isaac.core import World
from omni.isaac.universal_robots.controllers.pick_place_controller import PickPlaceController as ur10_PickPlaceController
from omni.isaac.core.objects import DynamicCuboid
'''
answer1 = '''
from omni.isaac.franka import Franka
from omni.isaac.core import World
from omni.isaac.core.objects import DynamicCuboid
from omni.isaac.franka.controllers import PickPlaceController 
import numpy as np
from omni.isaac.universal_robots import UR10
from omni.isaac.universal_robots.controllers.pick_place_controller import PickPlaceController as ur10_PickPlaceController
'''

que2 = '''
from omni.isaac.franka import Franka
from omni.isaac.core import World
from omni.isaac.core.objects import DynamicCuboid
from omni.isaac.franka.controllers import PickPlaceController 
import numpy as np
import numpy as np
from omni.isaac.universal_robots import UR10
import carb
import numpy as np
from omni.isaac.core import World
from omni.isaac.nucleus import get_assets_root_path
from omni.isaac.wheeled_robots.controllers.differential_controller import DifferentialController
from omni.isaac.wheeled_robots.robots import WheeledRobot
'''

answer2 = '''
from omni.isaac.franka import Franka
from omni.isaac.core import World
from omni.isaac.core.objects import DynamicCuboid
from omni.isaac.franka.controllers import PickPlaceController 
import numpy as np
from omni.isaac.universal_robots import UR10
import carb
from omni.isaac.nucleus import get_assets_root_path
from omni.isaac.wheeled_robots.controllers.differential_controller import DifferentialController
from omni.isaac.wheeled_robots.robots import WheeledRobot
'''
# 初始化一个 PromptSet 实例，使用定义好的变量作为参数
import_seg_prompt = PromptInfo(system=system_description, que_1=que1, answer_1=answer1, que_2=que2, answer_2=answer2 )
#print(import_seg_prompt.system)