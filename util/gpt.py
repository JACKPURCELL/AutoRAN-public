import openai
from openai import OpenAI
client = OpenAI()

import json
import time
import os
def ask_gpt(messages, gpt_model="gpt-4o-2024-11-20", ifjson=False, temp=0.6, try_times=0):
    try:
        try_times += 1
        if "o3" in gpt_model or "o1" in gpt_model or "o4" in gpt_model:
            if ifjson:
                completion = client.chat.completions.create(
                    model=gpt_model,
                    response_format={"type": "json_object"},
                    messages=messages,
                )
                content = completion.choices[0].message.content
                content = json.loads(content)
                if content is not None:
                    return content
            else:
                completion = client.chat.completions.create(
                    model=gpt_model,
                    messages=messages,
                )
                content = completion.choices[0].message.content
                if "I'm sorry" in content or "I’m sorry" in content or "sorry" in content.lower():
                    if try_times > 2:
                        return content
                    else:
                        if len(messages) == 1:
                            messages.insert(0, {"role": "system", "content": "You are a helpful assistant. You can help me by answering my questions. You can also ask me questions."})
                        print("Retrying ASK GPT...")
                        print(content)
                        return ask_gpt(messages, gpt_model, ifjson, temp, try_times)
                if content is not None:
                    return content
        else:
            if ifjson:
                completion = client.chat.completions.create(
                    model=gpt_model,
                    response_format={"type": "json_object"},
                    messages=messages,
                    temperature=temp,
                )
                content = completion.choices[0].message.content
                content = json.loads(content)
                if content is not None:
                    return content
            else:
                completion = client.chat.completions.create(
                    model=gpt_model,
                    messages=messages,
                    temperature=temp,
                )
                content = completion.choices[0].message.content
                if "I'm sorry" in content or "I’m sorry" in content:
                    if try_times > 3:
                        return content
                    else:
                        if len(messages) == 1:
                            messages.insert(0, {"role": "system", "content": "You are a helpful assistant. You can help me by answering my questions. You can also ask me questions."})
                        return ask_gpt(messages, gpt_model, ifjson, temp, try_times)
                if content is not None:
                    return content

    except openai.RateLimitError as e:
        # 从错误信息中提取等待时间
        wait_time = 30  # 默认等待时间
        if 'Please try again in' in str(e):
            try:
                wait_time = float(str(e).split('Please try again in')[1].split('s')[0].strip())
            except ValueError:
                pass
        print(f"Rate limit exceeded. Waiting for {wait_time} seconds before retrying...")
        time.sleep(wait_time)
        return ask_gpt(messages, gpt_model, ifjson, temp, try_times)  # 递归调用以重试请求

    except Exception as e:
        print(f"Error: {e}")
        if try_times > 2:
            print("Error in processing the request", messages)
            return None
        return ask_gpt(messages, gpt_model, ifjson, temp, try_times)  # 递归调用以重试请求

# Please install OpenAI SDK first: `pip3 install openai`


from google import genai

client_gemini = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def ask_gemini(messages, gpt_model="gemini-2.5-flash-preview-04-17", ifjson=False, temp=0.6, try_times=0):
    try:
        if ifjson:
            try_times += 1
            completion = client_gemini.models.generate_content(
                model=gpt_model,
                contents=messages,
                config={'response_mime_type': 'application/json'}
            )
            content = completion.text
            # print(content)
            
            content = json.loads(content)
            if content is not None:
                return content
        else:
            try_times += 1
            completion = client_gemini.models.generate_content(
                model=gpt_model,
                contents=messages,
            )
            content = completion.text
            if content is not None:
                return content
        

   

    except Exception as e:
        print(f"Error: {e}")
        if try_times > 4:
            print("Error in processing the request", messages)
            return None
        return ask_gemini(messages, gpt_model, ifjson, temp, try_times)  # 递归调用以重试请求
    
    
    
import os
client_ds = OpenAI(api_key=os.getenv("DEEPSEEK_API_KEY"), base_url="https://api.deepseek.com")

def ask_ds(messages, gpt_model="deepseek-chat", ifjson=False, temp=0.6, try_times=0):
    try:
        try_times += 1
        completion = client_ds.chat.completions.create(
            model=gpt_model,
            messages=messages,
            stream=False
        )
        content = completion.choices[0].message.content
        if content is not None:
            return content
        

    except openai.RateLimitError as e:
        # 从错误信息中提取等待时间
        wait_time = 30  # 默认等待时间
        if 'Please try again in' in str(e):
            try:
                wait_time = float(str(e).split('Please try again in')[1].split('s')[0].strip())
            except ValueError:
                pass
        print(f"Rate limit exceeded. Waiting for {wait_time} seconds before retrying...")
        time.sleep(wait_time)
        return ask_ds(messages, gpt_model, ifjson, temp, try_times)  # 递归调用以重试请求

    except Exception as e:
        print(f"Error: {e}")
        if try_times > 2:
            print("Error in processing the request", messages)
            return None
        return ask_ds(messages, gpt_model, ifjson, temp, try_times)  # 递归调用以重试请求
    



import os
client_qwen = OpenAI(
    # If environment variables are not configured, replace the following line with: api_key="sk-xxx",
    api_key=os.getenv("QWEN_API_KEY"), 
    base_url="https://dashscope-intl.aliyuncs.com/compatible-mode/v1",
)
def ask_qwen(messages, gpt_model="qwen2.5-32b-instruct", ifjson=False, temp=1.0, try_times=0):
    try:
        try_times += 1

        if ifjson:
            completion = client_qwen.chat.completions.create(
                model=gpt_model,
                response_format={"type": "json_object"},
                messages=messages,
                temperature=temp,
            )
            content = completion.choices[0].message.content
            content = json.loads(content)
            if content is not None:
                return content
        else:
            completion = client_qwen.chat.completions.create(
                model=gpt_model,
                messages=messages,
                temperature=temp,
            )
            content = completion.choices[0].message.content
            if "I'm sorry" in content or "I’m sorry" in content:
                if try_times > 3:
                    return content
                else:
                    if len(messages) == 1:
                        messages.insert(0, {"role": "system", "content": "You are a helpful assistant. You can help me by answering my questions. You can also ask me questions."})
                    return ask_qwen(messages, gpt_model, ifjson, temp, try_times)
            if content is not None:
                return content

    except openai.RateLimitError as e:
        # 从错误信息中提取等待时间
        wait_time = 30  # 默认等待时间
        if 'Please try again in' in str(e):
            try:
                wait_time = float(str(e).split('Please try again in')[1].split('s')[0].strip())
            except ValueError:
                pass
        print(f"Rate limit exceeded. Waiting for {wait_time} seconds before retrying...")
        time.sleep(wait_time)
        return ask_qwen(messages, gpt_model, ifjson, temp, try_times)  # 递归调用以重试请求

    except Exception as e:
        print(f"Error: {e}")
        if try_times > 2:
            print("Error in processing the request", messages)
            return None
        return ask_qwen(messages, gpt_model, ifjson, temp, try_times)  # 递归调用以重试请求
    
    
    
    
    
import os
client_qwen_vllm = OpenAI(
    # If environment variables are not configured, replace the following line with: api_key="sk-xxx",
    api_key="EMPTY", 
    base_url="http://localhost:8000/v1",
)
def ask_qwen_vllm(messages, gpt_model="huihui-ai/Qwen3-8B-abliterated", ifjson=False, temp=0.6, try_times=0,enable_thinking=True):
    try:
        try_times += 1

        if ifjson:
            completion = client_qwen_vllm.chat.completions.create(
                model=gpt_model,
                response_format={"type": "json_object"},
                messages=messages,
                temperature=temp,
                top_p=0.95,
                max_tokens=4096,
                extra_body={"chat_template_kwargs": {"enable_thinking": enable_thinking}},
    
            )
            content = completion.choices[0].message.content
            content = json.loads(content)
            if content is not None:
                # print("\n***ASK QWEN VLLM***\n")
                # print(content)
                # print("\n****************\n")
                return content
        else:
            completion = client_qwen_vllm.chat.completions.create(
                model=gpt_model,
                messages=messages,
                temperature=temp,
                top_p=0.95,
                max_tokens=4096,
                extra_body={"chat_template_kwargs": {"enable_thinking": enable_thinking}},
            )
            content = completion.choices[0].message.content
            if "I'm sorry" in content or "I’m sorry" in content:
                if try_times > 3:
                    return content
                else:
                    if len(messages) == 1:
                        messages.insert(0, {"role": "system", "content": "You are a helpful assistant. You can help me by answering my questions. You can also ask me questions."})
                    return ask_qwen_vllm(messages, gpt_model, ifjson, temp, try_times,enable_thinking)
            if content is not None:
                return content

    except openai.RateLimitError as e:
        # 从错误信息中提取等待时间
        wait_time = 5  # 默认等待时间
        if 'Please try again in' in str(e):
            try:
                wait_time = float(str(e).split('Please try again in')[1].split('s')[0].strip())
            except ValueError:
                pass
        print(f"Rate limit exceeded. Waiting for {wait_time} seconds before retrying...")
        time.sleep(wait_time)
        return ask_qwen_vllm(messages, gpt_model, ifjson, temp, try_times)  # 递归调用以重试请求

    except Exception as e:
        print(f"Error in ask_qwen: {e}")
        if try_times > 2:
            print("Error in processing the request", messages)
            return None
        return ask_qwen_vllm(messages, gpt_model, ifjson, temp, try_times)  # 递归调用以重试请求
    
if __name__ == "__main__":
    print(os.getenv("GEMINI_API_KEY"))
    print(ask_gemini("hello,return json {'hello':'world'}",ifjson=True))
    