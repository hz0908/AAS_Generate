import json


def main():
    data = [
        {
            "assetName": "franka机械臂",
            "assetDescription": "一种高精度的机械臂",
            "importSeg": (
                "from omni.isaac.franka import Franka\n"
                "from omni.isaac.core import World\n"
                "from omni.isaac.core.objects import DynamicCuboid\n"
                "from omni.isaac.franka.controllers import PickPlaceController as franka_PickPlaceController\n"
                "import numpy as np\n"
            ),
            "initSeg": {
                "initDescription": "将franka机械臂放置在[1,2,0]位置并初始化，其中变量名使用my_franka或以my_franka为前缀",
                "initCode": (
                    "my_franka = my_world.scene.add(Franka(prim_path='/World/Franka', name='my_franka', position=np.array([1,2,0])))\n"
                    "my_franka.gripper.set_joint_positions(my_franka.gripper.joint_opened_positions)\n"
                    "my_franka_controller = franka_PickPlaceController(\n"
                    "    name='pick_place_controller', gripper=my_franka.gripper, robot_articulation=my_franka\n"
                    ")\n"
                    "my_franka_articulation_controller = my_franka.get_articulation_controller()\n"
                )
            },
            "resetSeg": {
                "resetDescription": "franka机械臂的reset代码，其中变量名使用my_franka或以my_franka为前缀",
                "resetCode": (
                    "my_franka_controller.reset()\n"
                    "my_franka.gripper.set_joint_positions(my_franka.gripper.joint_opened_positions)\n"
                )
            },
            "physicsSeg": {
                "physicsDescription": "franka机械臂抓起方块放置在位置[-0.3, -0.3, 0.0515 / 2.0]处，其中franka机械臂使用变量名my_franka，方块使用变量名my_fancy_cube,可通过get_local_pose()方法获取位置信息",
                "physicsCode": (
                    "cube_position = my_fancy_cube.get_local_pose()[0]\n"
                    "goal_position = np.array([-0.3, -0.3, 0.0515 / 2.0])\n"
                    "current_joint_positions = my_franka.get_joint_positions()\n"
                    "actions = my_franka_controller.forward(\n"
                    "    picking_position=cube_position,\n"
                    "    placing_position=goal_position,\n"
                    "    current_joint_positions=current_joint_positions,\n"
                    ")\n"
                    "my_franka_articulation_controller.apply_action(actions)\n"
                )
            }
        },
        {
            "assetName": "jetbot小车",
            "assetDescription": "一个用于移动的智能小车",
            "importSeg": (
                "import carb\n"
                "import numpy as np\n"
                "from omni.isaac.core import World\n"
                "from omni.isaac.nucleus import get_assets_root_path\n"
                "from omni.isaac.wheeled_robots.controllers.differential_controller import DifferentialController\n"
                "from omni.isaac.wheeled_robots.robots import WheeledRobot\n"
            ),
            "initSeg": {
                "initDescription": "Initialization for jetbot小车",
                "initCode": (
                    "assets_root_path = get_assets_root_path()\n"
                    "if assets_root_path is None:\n"
                    "    carb.log_error('Could not find Isaac Sim assets folder')\n"
                    "jetbot_asset_path = assets_root_path + '/Isaac/Robots/Jetbot/jetbot.usd'\n"
                    "my_jetbot = my_world.scene.add(\n"
                    "    WheeledRobot(\n"
                    "        prim_path='/World/Jetbot',\n"
                    "        name='my_jetbot',\n"
                    "        wheel_dof_names=['left_wheel_joint', 'right_wheel_joint'],\n"
                    "        create_robot=True,\n"
                    "        usd_path=jetbot_asset_path,\n"
                    "        position=np.array([0, 0.0, 2.0]),\n"
                    "    )\n"
                    ")\n"
                    "my_jetbot_controller = DifferentialController(name='simple_control', wheel_radius=0.03, wheel_base=0.1125)\n"
                )
            },
            "resetSeg": {
                "resetDescription": "jetbot小车的reset代码，其中变量名使用my_jetbot或以my_jetbot为前缀",
                "resetCode": (
                    "my_jetbot_controller.reset()\n"
                )
            },
            "physicsSeg": {
                "physicsDescription": "jetbot小车以0.05m/s的速度移动，车轮转角为0，即向前移动，其中jetbot小车使用变量名my_jetbot",
                "physicsCode": (
                    "my_jetbot.apply_wheel_actions(my_jetbot_controller.forward(command=[0.05, 0]))\n"
                )
            }
        },
        {
            "assetName": "ur10机械臂",
            "assetDescription": "另一种性能优良的机械臂",
            "importSeg": "lib4",
            "initSeg": {
                "initDescription": "将ur10机械臂放置在[0,0,0]并初始化，其中变量名使用ur10_arm或以ur10_arm为前缀",
                "initCode": (
                    "ur10_arm = my_world.scene.add(UR10(prim_path='/World/UR10', name='ur10_arm', positon=np.array([0, 0, 0]), gripper_usd=None, attach_gripper=True))\n"
                    "ur10_arm.set_joints_default_state(\n"
                    "    positions=np.array([-np.pi / 2, -np.pi / 2, -np.pi / 2, -np.pi / 2, np.pi / 2, 0])\n"
                    ")\n"
                    "ur10_arm.gripper.set_default_state(opened=True)\n"
                    "ur10_arm_controller = ur10_PickPlaceController(name='pick_place_controller', gripper=ur10_arm.gripper, robot_articulation=ur10_arm)\n"
                    "ur10_arm_articulation_controller = ur10_arm.get_articulation_controller()\n"
                )
            },
            "resetSeg": {
                "resetDescription": "ur10机械臂的reset代码，其中变量名使用ur10_arm或以ur10_arm为前缀",
                "resetCode": (
                    "ur10_arm_controller.reset()\n"
                    "ur10_arm.set_joints_default_state(\n"
                    "    positions=np.array([-np.pi / 2, -np.pi / 2, -np.pi / 2, -np.pi / 2, np.pi / 2, 0])\n"
                    ")\n"
                )
            },
            "physicsSeg": {
                "physicsDescription": "ur10机械臂将方块抓起放置在位置[0.7, 0.7, 0.0515 / 2.0]处，其中ur10机械臂使用变量名ur10_arm,方块使用变量名cube，可通过get_local_pose()方法获取位置信息",
                "physicsCode": (
                    "actions = ur10_arm_controller.forward(\n"
                    "    picking_position=cube.get_local_pose()[0],\n"
                    "    placing_position=np.array([0.7, 0.7, 0.0515 / 2.0]),\n"
                    "    current_joint_positions=ur10_arm.get_joint_positions(),\n"
                    "    end_effector_offset=np.array([0, 0, 0.02]),\n"
                    ")\n"
                    "ur10_arm_articulation_controller.apply_action(actions)\n"
                )
            }
        },
        {
            "assetName": "物料盘",
            "assetDescription": "一个盘子",
            "importSeg": "lib4",
            "initSeg": {
                "initDescription": "初始化一个大小为[0.0515, 0.0515, 0.0515]的物块，放置在位置[0.3, 0.3, 0.3]",
                "initCode": (
                    "cube = my_world.scene.add(\n"
                    "    DynamicCuboid(\n"
                    "        name='cube',\n"
                    "        position=np.array([0.3, 0.3, 0.3]),\n"
                    "        prim_path='/World/Cube',\n"
                    "        scale=np.array([0.0515, 0.0515, 0.0515]),\n"
                    "        size=1.0,\n"
                    "        color=np.array([0, 0, 1]),\n"
                    "    )\n"
                )
            },
            "resetSeg": {
                "resetDescription": "Reset for 物料盘",
                "resetCode": (
                    ":\n"
                )
            },
            "physicsSeg": {
                "physicsDescription": "Physics operations for 物料盘",
                "physicsCode": (
                    "def physics_ur10():\n"
                    "    pass"
                )
            }
        },
        {
            "assetName": "物块",
            "assetDescription": "一个方块",
            "importSeg": "from omni.isaac.core.objects import DynamicCuboid\n",
            "initSeg": {
                "initDescription": "初始化一个的物块，放置在位置[0.3, 0.3, 0.3]，变量名使用cube或以cube为前缀",
                "initCode": (
                    "cube = my_world.scene.add(\n"
                    "    DynamicCuboid(\n"
                    "        name='cube',\n"
                    "        position=np.array([0.3, 0.3, 0.3]),\n"
                    "        prim_path='/World/Cube',\n"
                    "        scale=np.array([0.0515, 0.0515, 0.0515]),\n"
                    "        size=1.0,\n"
                    "        color=np.array([0, 0, 1]),\n"
                    "    )\n"
                )
            },
            "resetSeg": {
                "resetDescription": "Reset for 物块A",
                "resetCode": (
                    "\n"
                )
            },
            "physicsSeg": {
                "physicsDescription": "Physics operations for 物块A",
                "physicsCode": (
                    "\n"
                )
            }
        }
    ]
    # 将数据转换为 JSON 格式的字符串
    json_data = json.dumps(data, indent=4, ensure_ascii=False)
    # 将 JSON 数据写入文件
    with open('assets.json', 'w', encoding='utf-8') as f:
        f.write(json_data)


if __name__ == "__main__":
    main()