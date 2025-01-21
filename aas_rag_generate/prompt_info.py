class PromptInfo:
    def __init__(self, system="你是一个优秀的人工智能" , que_1="问题示例1", answer_1="答案1", que_2="问题示例2 ", answer_2="答案2"):
        # 大模型的角色定位描述
        self.system = system
        # 示例 1 的输入
        self.que_1 = que_1
        # 示例 1 的输出
        self.answer_1 = answer_1
        # 示例 2 的输入
        self.que_2 = que_2
        # 示例 2 的输出
        self.answer_2 = answer_2


