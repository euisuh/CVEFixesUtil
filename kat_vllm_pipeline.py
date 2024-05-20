import subprocess
import time
import argparse
import os
import json
from utils import *
from prompts_kat import *
import pandas as pd

def exp_R1(df, cwe_map, model):
    prompts_before = [promptR1(df.func_before.iloc[i], cwe_map.get(df['exp_cwe_id'].iloc[i][4:])['name']) for i in range(df.shape[0])]
    prompts_after = [promptR1(df.func_after.iloc[i], cwe_map.get(df['exp_cwe_id'].iloc[i][4:])['name']) for i in range(df.shape[0])]

    prompts = prompts_before + prompts_after
    
    res10 = inferModelVllm(model[1], prompts)

    res_before = []
    res_after = []
    
    n = len(res10)
    df['res_before'] = res10[:n//2]
    df['res_after'] = res10[n//2:]

    df.to_csv(f'kat_res/res_R1_{model[0]}.csv', index=False)  

def exp_S1(df, cwe_map, model):
    prompts_before = [promptS1(df.func_before.iloc[i], cwe_map.get(df['exp_cwe_id'].iloc[i][4:])['name']) for i in range(df.shape[0])]
    prompts_after = [promptS1(df.func_after.iloc[i], cwe_map.get(df['exp_cwe_id'].iloc[i][4:])['name']) for i in range(df.shape[0])]

    prompts = prompts_before + prompts_after
    
    res10 = inferModelVllm(model[1], prompts)

    res_before = []
    res_after = []

    n = len(res10)
    df['res_before'] = res10[:n//2]
    df['res_after'] = res10[n//2:]

    df.to_csv(f'kat_res/res_S1_{model[0]}.csv', index=False)  

def main():
    parser = argparse.ArgumentParser(description='Process command line arguments.')

    parser.add_argument('--cuda-visible-devices', dest='cuda_visible_devices', type=int, help='Index of the CUDA visible device')
    parser.add_argument('--experiment-name', dest='experiment_name', type=str, help='Experiment name')
    
    args = parser.parse_args()

    experiment_name = args.experiment_name
    os.environ["CUDA_VISIBLE_DEVICES"] = str(args.cuda_visible_devices)

    models = [
        ('llama3', 'meta-llama_Meta-Llama-3-8B-Instruct/'),
        # ('codeLlama', 'meta-llama_CodeLlama-7b-hf/'),
        # ('qwen', 'Qwen_Qwen1.5-7B-Chat/'),
        # ('codeQwen', 'Qwen_CodeQwen1.5-7B-Chat/'),
        # ('gemma', 'google_gemma-7b/'),
        # ('mistral', 'mistralai_Mistral-7B-Instruct-v0.2/'),
        # ('deepSeekCoder', 'deepseek-ai_deepseek-coder-6.7b-instruct/'),
    ]

    with open("cwe25.json", 'r') as file:
        cwe25 = json.load(file)
        cwe_map = {item['id']: {'name': item['name'], 'description': item['description']} for item in cwe25}

    df = pd.read_csv('vulC7_test.csv')
        
    

    for model in models:
        if experiment_name == 'R1':
            exp_R1(df, cwe_map, model)
        if experiment_name == 'S1':
            exp_S1(df, cwe_map, model)
            
        print(f"Compmleted model inference for {model[0]}")

if __name__ == "__main__":
    main()
