import json


def main():
    data = [
        {
            "assetName": "franka机械臂",
            "assetDescription": "一种高精度的机械臂",
            "importSeg": (
                "import numpy as np\n"
                "from omni.isaac.universal_robots import UR10\n"
                "from omni.isaac.core import World\n"
                "from omni.isaac.universal_robots.controllers.pick_place_controller import PickPlaceController as ur10_PickPlaceController\n"
                "from omni.isaac.core.objects import DynamicCuboid"
            ),
            "initSeg": {
                "initDescription": "Initialization for franka机械臂",
                "initCode": (
                    "def init_franka():\n"
                    "    pass"
                )
            },
            "resetSeg": {
                "resetDescription": "Reset for franka机械臂",
                "resetCode": (
                    "def reset_franka():\n"
                    "    pass"
                )
            },
            "physicsSeg": {
                "physicsDescription": "Physics operations for franka机械臂",
                "physicsCode": (
                    "def physics_franka():\n"
                    "    pass"
                )
            }
        },
        {
            "assetName": "jetbot小车",
            "assetDescription": "一个用于移动的智能小车",
            "importSeg": "lib3",
            "initSeg": {
                "initDescription": "Initialization for jetbot小车",
                "initCode": (
                    "def init_jetbot():\n"
                    "    pass"
                )
            },
            "resetSeg": {
                "resetDescription": "Reset for jetbot小车",
                "resetCode": (
                    "def reset_jetbot():\n"
                    "    pass"
                )
            },
            "physicsSeg": {
                "physicsDescription": "Physics operations for jetbot小车",
                "physicsCode": (
                    "def physics_jetbot():\n"
                    "    pass"
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
                    "ur10_arm = my_world.scene.add(UR10(prim_path='/World/UR10', name='ur10_arm', gripper_usd=None, attach_gripper=True))\n"
                    "ur10_arm.set_joints_default_state(\n"
                    "    positions=np.array([-np.pi / 2, -np.pi / 2, -np.pi / 2, -np.pi / 2, np.pi / 2, 0])\n"
                    ")\n"
                    "ur10_arm.gripper.set_default_state(opened=True)\n"
                    "ur10_arm_controller = ur10_PickPlaceController(name='pick_place_controller', gripper=ur10_arm.gripper, robot_articulation=ur10_arm)\n"
                    "ur10_arm_articulation_controller = ur10_arm.get_articulation_controller()"
                )
            },
            "resetSeg": {
                "resetDescription": "ur10机械臂的reset代码，其中变量名使用ur10_arm或以ur10_arm为前缀",
                "resetCode": (
                    "ur10_arm_controller.reset()\n"
                    "ur10_arm.set_joints_default_state(\n"
                    "    positions=np.array([-np.pi / 2, -np.pi / 2, -np.pi / 2, -np.pi / 2, np.pi / 2, 0])\n"
                    ")"
                )
            },
            "physicsSeg": {
                "physicsDescription": "Physics operations for ur10机械臂",
                "physicsCode": (
                    "actions = ur10_arm_controller.forward(\n"
                    "    picking_position=cube.get_local_pose()[0],\n"
                    "    placing_position=np.array([0.7, 0.7, 0.0515 / 2.0]),\n"
                    "    current_joint_positions=ur10_arm.get_joint_positions(),\n"
                    "    end_effector_offset=np.array([0, 0, 0.02]),\n"
                    ")\n"
                    "ur10_arm_articulation_controller.apply_action(actions)"
                )
            }
        },
        {
            "assetName": "物料盘",
            "assetDescription": "一个盘子",
            "importSeg": "lib4",
            "initSeg": {
                "initDescription": "Initialization for 物料盘",
                "initCode": (
                    "def init_ur10():\n"
                    "    pass"
                )
            },
            "resetSeg": {
                "resetDescription": "Reset for 物料盘",
                "resetCode": (
                    "def reset_ur10():\n"
                    "    pass"
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
            "assetName": "物块A",
            "assetDescription": "一个方块",
            "importSeg": "lib4",
            "initSeg": {
                "initDescription": "Initialization for 物块A",
                "initCode": (
                    "def init_ur10():\n"
                    "    pass"
                )
            },
            "resetSeg": {
                "resetDescription": "Reset for 物块A",
                "resetCode": (
                    "def reset_ur10():\n"
                    "    pass"
                )
            },
            "physicsSeg": {
                "physicsDescription": "Physics operations for 物块A",
                "physicsCode": (
                    "def physics_ur10():\n"
                    "    pass"
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