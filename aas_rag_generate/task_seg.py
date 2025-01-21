from prompt_info import PromptInfo
# 为每个参数定义单独的变量
system_description = "你是一个语义分析专家，能够从我给出的描述的任务流程中按照执行顺序划分出各个子任务，并将分析结果以json格式输出"
question_1 = "scalar机械臂A将物块B抓起放到传送带C上，传送带C将物块B运输到delata机器人D前，然后delata机器人D将物块抓起放到物料盘上"
answer_1 = '''
{
  "task_count": 3,
  "task_set": [
    {
      "task_number": 1,
      "task_description": "scalar机械臂A将物块B抓起放到传送带C上",
      "asset_used": [
        {
          "user_description": "scalar机械臂A"
        },
        {
          "user_description": "物块B"
        },
        {
          "user_description": "传送带C"
        }
      ]
    },
    {
      "task_number": 2,
      "task_description": "传送带C将物块B运输到delata机器人D前",
      "asset_used": [
        {
          "user_description": "传送带C"
        },
        {
          "user_description": "物块B"
        },
        {
          "user_description": "delata机器人D"
        }
      ]
    },
    {
      "task_number": 3,
      "task_description": "delata机器人D将物块抓起放到物料盘上",
      "asset_used": [
        {
          "user_description": "delata机器人D"
        },
        {
          "user_description": "物块B"
        },
        {
          "user_description": "物料盘"
        }
      ]
    }
  ]
}
'''
question_2 = "frank机械臂将一个方块放置在jetbot前方，然后jetbot推动方块移动到ur10机械臂附近，ur10机械臂将方块抓起放到另外一个位置"
answer_2 = '''
{
    "task_count":3,
    "task_set":[
        {
            "task_number":1,
            "task_description":"frank机械臂将一个方块放置在jetbot前方",
            "asset_used":[
                {
                    "user_description":"frank机械臂"
                },
                {
                    "user_description":"方块"
                },
                {
                    "user_description":"jetbot"
                }
            ]
        },
        {
            "task_number":2,
            "task_description":"jetbot推动方块移动到ur10机械臂附近",
            "asset_used":[
                {
                    "user_description":"jetbot"
                },
                {
                    "user_description":"方块"
                },
                {
                    "user_description":"ur10机械臂"
                }
            ]
        },
        {
            "task_number":3,
            "task_description":"ur10机械臂将方块抓起放到另外一个位置",
            "asset_used":[
                {
                    "user_description":"ur10机械臂"
                },
                {
                    "user_description":"方块"
                }
            ]
        }
    ]
}
'''


# 初始化一个 PromptSet 实例，使用定义好的变量作为参数
task_seg_prompt = PromptInfo(system_description, question_1, answer_1, question_2, answer_2)
#print(task_seg_prompt.system)