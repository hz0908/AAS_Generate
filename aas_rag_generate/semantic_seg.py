from prompt_info import PromptInfo
# 为每个参数定义单独的变量
system_description = "你是制造业领域语义分析专家，需根据“设备运行流程”描述，分析其中涉及的设备种类、每种设备数量，并赋予其独特程序变量名。最终以规范的 JSON 格式输出结果。"
question_1 = "frank机械臂将一个方块放置在jetbot前方，然后jetbot推动方块移动到ur10机械臂附近，ur10机械臂将方块抓起放到另外一个位置"
answer_1 = '''{
    "equipmentInfo": [
        {
            "equipmentName":"frank 机械臂",
            "quantity":1,
            "instanceEquipment":[
                {
                    "descriptionName":"frank 机械臂",
                    "programName":"frank_arm"
                }
            ]
        },
        {
            "equipmentName":"jetbot",
            "quantity":1,
            "instanceEquipment":[
                {
                    "descriptionName":"jetbot",
                    "programName":"jetbot_1"
                }
            ]
        },
        {
            "equipmentName":"ur10 机械臂",
            "quantity":1,
            "instanceEquipment":[
                {
                    "descriptionName":"ur10 机械臂",
                    "programName":"ur10_arm"
                }
            ]
        }
    ]
}'''
question_2 = "franka机械臂A将药瓶夹起放置在工作台上，然后ur10机械臂将工作台上的药瓶夹起放置到托盘上，随后franka机械臂B将托盘上的药瓶夹起放置到运输车上"
answer_2 = '''{
    "equipmentInfo":[
        {
            "equipmentName":"franka 机械臂",
            "quantity":2,
            "instanceEquipment":[
                {
                    "descriptionName":"franka 机械臂 A",
                    "programName":"franka_arm_A"
                },
                {
                    "descriptionName":"franka 机械臂 B",
                    "programName":"franka_arm_B"
                }
            ]
        },
        {
            "equipmentName":"ur10 机械臂",
            "quantity":1,
            "instanceEquipment":[
                {
                    "descriptionName":"ur10 机械臂",
                    "programName":"ur10_arm"
                }
            ]
        },
        {
            "equipmentName":"工作台",
            "quantity":1,
            "instanceEquipment":[
                {
                    "descriptionName":"工作台",
                    "programName":"workbench"
                }
            ]
        },
        {
            "equipmentName":"托盘",
            "quantity":1,
            "instanceEquipment":[
                {
                    "descriptionName":"托盘",
                    "programName":"pallet"
                }
            ]
        },
        {
            "equipmentName":"运输车",
            "quantity":1,
            "instanceEquipment":[
                {
                    "descriptionName":"运输车",
                    "programName":"transport_vehicle"
                }
            ]
        }
    ]
}'''


# 初始化一个 PromptSet 实例，使用定义好的变量作为参数
semantic_seg_prompt = PromptInfo(system_description, question_1, answer_1, question_2, answer_2)
#print(semantic_seg_prompt.system)