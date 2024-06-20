import random
from http import HTTPStatus

import dashscope

dashscope.api_key='sk-cc8790e15ef24a0c950fe829f0a7af55'

def sample_sync_call():
    prompt_text = '用萝卜、土豆、茄子做饭，给我个菜谱。'
    resp = dashscope.Generation.call(
        model='qwen-turbo',
        prompt=prompt_text
    )

    if resp.status_code == HTTPStatus.OK:
        print(resp.output)  # The output text
        print(resp.usage)  # The usage information
    else:
        print(resp.code)  # The error code.
        print(resp.message)  # The error message.


def sample_call_streaming():
    prompt_text = '用萝卜、土豆、茄子做饭，给我个菜谱。'
    response_generator = dashscope.Generation.call(
        model='qwen-turbo',
        prompt=prompt_text,
        stream=True,
        top_p=0.8)
    # When stream=True, the return is Generator,
    # need to get results through iteration
    for response in response_generator:
        if response.status_code == HTTPStatus.OK:
            print(response.output)  # The output text
            print(response.usage)  # The usage information
        else:
            print(response.code)  # The error code.
            print(response.message)  # The error message.



def sample_sync_call_streaming():
    prompt_text = '用萝卜、土豆、茄子做饭，给我个菜谱。'
    model=Qwen
    response_generator = dashscope.Generation.call(
        model=model,
        prompt=prompt_text,
        stream=True,
        top_p=0.8)

    head_idx = 0
    for resp in response_generator:
        paragraph = resp.output['text']
        print("\r%s" % paragraph[head_idx:len(paragraph)], end='')
        if(paragraph.rfind('\n') != -1):
            head_idx = paragraph.rfind('\n') + 1




if __name__ == '__main__':
    # sample_sync_call()


    sample_sync_call_streaming()
