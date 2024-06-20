from http import HTTPStatus
import dashscope
import os
dashscope.api_key='sk-cc8790e15ef24a0c950fe829f0a7af55'
def tokenizer():
    response = dashscope.Tokenization.call(
        model='qwen-turbo',

        messages=[{'role': 'user', 'content': '你好？'}],
        api_key=os.getenv("DASHSCOPE_API_KEY"),
        )
    if response.status_code == HTTPStatus.OK:
        # print('Result is: %s' % response)
        print(response.usage)
    else:
        print('Failed request_id: %s, status_code: %s, code: %s, message:%s' %
              (response.request_id, response.status_code, response.code,
               response.message))


if __name__ == '__main__':
    tokenizer()