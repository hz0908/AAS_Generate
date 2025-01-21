from prompt_info import PromptInfo
# 为每个参数定义单独的变量
system_description = "你是一个高级的python工程师，能够对用户提供的导入各pyhton库的代码进行分析，去除一些重复的库导入代码，输出最终的去重后的代码"


# 初始化一个 PromptSet 实例，使用定义好的变量作为参数
import_seg_prompt = PromptInfo(system_description)
#print(import_seg_prompt.system)