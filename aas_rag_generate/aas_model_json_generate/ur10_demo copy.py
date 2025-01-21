from isaacsim import SimulationApp

simulation_app = SimulationApp({"headless": False})

import numpy as np
from omni.isaac.universal_robots import UR10
from omni.isaac.core import World
from omni.isaac.universal_robots.controllers.pick_place_controller import PickPlaceController as ur10_PickPlaceController
from omni.isaac.core.objects import DynamicCuboid

my_world = World(stage_units_in_meters=1.0)
ur10_arm = my_world.scene.add(UR10(prim_path="/World/UR10", name="ur10_arm", gripper_usd=None, attach_gripper=True))
my_world.scene.add_default_ground_plane()
cube = my_world.scene.add(
    DynamicCuboid(
        name="cube",
        position=np.array([0.3, 0.3, 0.3]),
        prim_path="/World/Cube",
        scale=np.array([0.0515, 0.0515, 0.0515]),
        size=1.0,
        color=np.array([0, 0, 1]),
    )
)

ur10_arm.set_joints_default_state(
    positions=np.array([-np.pi / 2, -np.pi / 2, -np.pi / 2, -np.pi / 2, np.pi / 2, 0])
)
ur10_arm.gripper.set_default_state(opened=True)
my_world.reset()

ur10_arm_controller = ur10_PickPlaceController(name="pick_place_controller", gripper=ur10_arm.gripper, robot_articulation=ur10_arm)
ur10_arm_articulation_controller = ur10_arm.get_articulation_controller()


reset_needed = False
while simulation_app.is_running():
    my_world.step(render=True)
    if my_world.is_stopped() and not reset_needed:
        reset_needed = True
    if my_world.is_playing():
        if reset_needed:
            my_world.reset()
            ur10_arm_controller.reset()
            reset_needed = False
        observations = my_world.get_observations()
        actions = ur10_arm_controller.forward(
            picking_position=cube.get_local_pose()[0],
            placing_position=np.array([0.7, 0.7, 0.0515 / 2.0]),
            current_joint_positions=ur10_arm.get_joint_positions(),
            end_effector_offset=np.array([0, 0, 0.02]),
        )
        if ur10_arm_controller.is_done():
            print("done picking and placing")
        ur10_arm_articulation_controller.apply_action(actions)

simulation_app.close()