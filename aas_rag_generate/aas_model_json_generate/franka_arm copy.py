from isaacsim import SimulationApp

simulation_app = SimulationApp({"headless": False})



from omni.isaac.franka import Franka
from omni.isaac.core import World
from omni.isaac.core.objects import DynamicCuboid
from omni.isaac.franka.controllers import PickPlaceController
import numpy as np




my_world = World(stage_units_in_meters=1.0)

my_franka = my_world.scene.add(Franka(prim_path="/World/Franka", name="my_franka", position=[1,2,0]))
my_franka.gripper.set_joint_positions(my_franka.gripper.joint_opened_positions)

my_franka_controller = PickPlaceController(
    name="pick_place_controller", gripper=my_franka.gripper, robot_articulation=my_franka
)
articulation_controller = my_franka.get_articulation_controller()



reset_needed = False
while simulation_app.is_running():
    my_world.step(render=True)
    if my_world.is_stopped() and not reset_needed:
        reset_needed = True
    if my_world.is_playing():
        if reset_needed:
            my_world.reset()
            my_franka_controller.reset()
            my_franka.gripper.set_joint_positions(my_franka.gripper.joint_opened_positions)
            reset_needed = False
        cube_position, _ = my_fancy_cube.get_world_pose()
        goal_position = np.array([-0.3, -0.3, 0.0515 / 2.0])
        current_joint_positions = my_franka.get_joint_positions()
        actions = my_franka_controller.forward(
            picking_position=cube_position,
            placing_position=goal_position,
            current_joint_positions=current_joint_positions,
        )
        if my_franka_controller.is_done():
            print("done picking and placing")
        articulation_controller.apply_action(actions)

simulation_app.close()