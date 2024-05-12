import argparse
import requests
import pandas as pd
from prompt import *
from tqdm import tqdm

def inferModel(prompt='This is a cake recipe:\n\n', port=5001, temperature=0.8, max_tokens=200):
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

def main():
    parser = argparse.ArgumentParser(description='Process command line arguments.')

    parser.add_argument('--listen-port', dest='listen_port', type=int, help='Port to listen on')
    parser.add_argument('--model-name', dest='model_name', type=str, help='Name of the model')

    args = parser.parse_args()

    listen_port = args.listen_port
    model_name = args.model_name

    df = pd.read_csv('vul7.csv')

    res_before = []
    res_after = []
    
    for i in tqdm(range(df.shape[0])):
        res_before.append(inferModel(prompt1(df.func_before.iloc[i]), port=listen_port, max_tokens=20))
        res_after.append(inferModel(prompt1(df.func_after.iloc[i]), port=listen_port, max_tokens=20))
        
    df['res_func_before'] = res_before
    df['res_func_after'] = res_after
    
    df.to_csv(f'res_vulC7_{model_name}.csv', index=False)


if __name__ == "__main__":
    main()
    