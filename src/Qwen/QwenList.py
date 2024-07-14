class QwenList:
    def __init__(self):
        self.models ={"qwen-long":"qwen-long","qwen-turbo":"qwen-turbo","qwen-plus":"qwen-plus","qwen-max":"qwen-max",
                      "qwen-max-0428":"qwen-max-0428","qwen-max-0403":"qwen-max-0403","qwen-max-longcontext":"qwen-max-longcontext"}
    def getQwenList(self):
        return self.models