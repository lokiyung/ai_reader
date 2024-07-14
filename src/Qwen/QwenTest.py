import random
from http import HTTPStatus

import requests
import os
import re

from src.Qwen.QwenList import QwenList
from src.Tools import FileUtils

api_key='sk-cc8790e15ef24a0c950fe829f0a7af55'
# api_key = os.getenv("DASHSCOPE_API_KEY")
url = 'https://dashscope.aliyuncs.com/api/v1/services/aigc/text-generation/generation'
headers = {'Content-Type': 'application/json',
           'Authorization': f'Bearer {api_key}'
           # ,'X-DashScope-SSE': 'enable'} 流式输出
           }

messages = [
    {
        "role": "system",
        "content": "你是一个擅长总结，文字功底很好的台本作家"
    }
]

    # 封装模型的响应函数
def get_response(last_messages):
    body = {
        'model': 'qwen-turbo',
        "input": {
            "messages": last_messages
        },
        "parameters": {
            "result_format": "message"
        }
    }
    response = requests.post(url, headers=headers, json=body)
    return response.json()



if __name__ == '__main__':
    # 您可以在此修改对话轮数，当前为3轮对话
    for i in range(3):
        context=FileUtils.read_file(r'C:\Users\lilyung\Desktop\new.txt')
        UserInput = context
        messages.append({
            "role": "user",
            "content": UserInput
        })
        response = get_response(messages)
        assistant_output = response['output']['choices'][0]['message']
        print("用户输入：", UserInput)
        print(f"模型输出：{assistant_output['content']}\n")
        messages.append(assistant_output)