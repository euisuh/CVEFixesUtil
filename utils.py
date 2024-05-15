import requests
from vllm import LLM, SamplingParams

def inferModelVllm(model, prompts, temperature=0.8, top_p=0.9):
    sampling_params = SamplingParams(temperature=temperature, top_p=top_p)
    
    llm = LLM(model=f"../text-generation-webui/models/{model}", dtype='half')
    outputs = llm.generate(prompts, sampling_params)

    res = []
    for output in outputs:
        prompt = output.prompt
        generated_text = output.outputs[0].text
        res.append(generated_text)

    return res

def inferModel(prompt='This is a cake recipe:\n\n', port=5000, temperature=0.8, max_tokens=200):
    url = f'http://127.0.0.1:{port}/v1/completions'
    headers = {'Content-Type': 'application/json'}
    
    data = {
        "prompt": prompt,
        "max_tokens": max_tokens,
        "temperature": temperature,
        "top_p": 0.9,
        "seed": 10
    }
    
    response = requests.post(url, headers=headers, json=data)
    
    if response.status_code == 200:
        try:
            return response.json()['choices'][0]['text']
        except:
            return 'FAILED TO PARSE RESPONSE'
    else:
        return response.text


def inferSystemModel(prompt='This is a cake recipe:\n\n', system_prompt="You are a helpful assistant.", port=5000, temperature=0.8, max_tokens=200):
    url = f'http://127.0.0.1:{port}/v1/chat/completions'
    headers = {'Content-Type': 'application/json'}
    
    data = {
        "messages": [
            {
                "role": "system",
                "content": system_prompt
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        "max_tokens": max_tokens,
        "temperature": temperature,
        "top_p": 0.9,
        "seed": 10,
        "mode": 'instruct',
    }
    
    response = requests.post(url, headers=headers, json=data)
    
    if response.status_code == 200:
        try:
            return response.json()['choices'][0]['message']['content']
        except:
            return 'FAILED TO PARSE RESPONSE'
    else:
        return response.text


def extract_cwe(possible_options, cwe25):
    for cwe in cwe25:
        for possible_id in possible_options:
            possible_id = possible_id[4:]

            if possible_id == cwe['id']:
                return cwe['id'], cwe['name'], cwe['description']

    return '', '', ''