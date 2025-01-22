from prompt_info import PromptInfo
# 为每个参数定义单独的变量
system_description = "你是制造业领域语义分析专家，需根据“设备运行流程”描述，分析其中涉及的设备种类、每种设备数量，并赋予其独特程序变量名。最终以规范的 JSON 格式输出结果。"
question_1 = "scara机械臂将一个物块放置在agv小车前方，然后agv小车推动物块移动到ur10机械臂附近，ur10机械臂将物块抓起放到另外一个位置。其中scara机械臂的初始位置是[0,0,0],物快的初始位置是[0.3,0.3,0]，agv小车的初始位置是[1,1,0],ur10机械臂的初始位置是[1.-3,0]"
answer_1 = '''{
    "equipmentInfo": [
        {
            "equipmentName":"scara机械臂",
            "quantity":1,
            "instanceEquipment":[
                {
                    "descriptionName":"scara机械臂",
                    "programName":"scara_arm",
                    "position": "[0, 0, 0]"
                }
            ]
        },
        {
            "equipmentName":"agv小车",
            "quantity":1,
            "instanceEquipment":[
                {
                    "descriptionName":"agv",
                    "programName":"agv_1",
                    "position": "[1, 1, 0]"
                }
            ]
        },
        {
            "equipmentName":"ur10机械臂",
            "quantity":1,
            "instanceEquipment":[
                {
                    "descriptionName":"ur10机械臂",
                    "programName":"ur10_arm",
                    "position": "[1, -3, 0]"
                }
            ]
        },
        {
            "equipmentName":"物块",
            "quantity":1,
            "instanceEquipment":[
                {
                    "descriptionName":"物块",
                    "programName":"cube",
                    "position": "[0.3, 0.3, 0]"
                }
            ]
        }
    ]
}'''
question_2 = "franka机械臂A将药瓶夹起放置在工作台上，然后ur10机械臂将工作台上的药瓶夹起放置到托盘上，随后franka机械臂B将托盘上的药瓶夹起放置到运输车上"
answer_2 = '''{
    "equipmentInfo":[
        {
            "equipmentName":"franka机械臂",
            "quantity":2,
            "instanceEquipment":[
                {
                    "descriptionName":"franka机械臂A",
                    "programName":"franka_arm_A"
                },
                {
                    "descriptionName":"franka机械臂B",
                    "programName":"franka_arm_B"
                }
            ]
        },
        {
            "equipmentName":"ur10机械臂",
            "quantity":1,
            "instanceEquipment":[
                {
                    "descriptionName":"ur10机械臂",
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