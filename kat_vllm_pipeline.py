import subprocess
import time
import argparse
import os


def main():
    parser = argparse.ArgumentParser(description='Process command line arguments.')
    parser.add_argument('--cuda-visible-devices', dest='cuda_visible_devices', type=int, help='Index of the CUDA visible device')
    parser.add_argument('--experiment-name', dest='experiment_name', type=str, help='Experiment name')
    
    args = parser.parse_args()
    experiment_name = args.experiment_name

    print('hello')
    
    models = [
        # ('codeLlama', 'meta-llama_CodeLlama-7b-hf/'),
        # ('qwen', 'Qwen_Qwen1.5-7B-Chat/'),
        # ('codeQwen', 'Qwen_CodeQwen1.5-7B-Chat/'),
        # ('gemma', 'google_gemma-7b/'),
        # ('artigenz', 'Artigenz_Artigenz-Coder-DS-6.7B/'),
        # ('mistral', 'mistralai_Mistral-7B-Instruct-v0.2/'),
        # ('deepSeekCoder', 'deepseek-ai_deepseek-coder-6.7b-instruct/'),
        ('llama3', 'meta-llama_Meta-Llama-3-8B-Instruct/'),
    ]

    for model in models:
        print(f'Begin experiment for {model[0]}')
        script1_command = f"python kat_vllm_experiment.py --cuda-visible-devices {args.cuda_visible_devices} --experiment-name {experiment_name} --model {model[0]} --model-path {model[1]}"
        script1_process = subprocess.Popen(script1_command, shell=True)
        script1_process.wait()
        print(f'End experiment for {model[0]}')
    
        time.sleep(10)
    
if __name__ == "__main__":
    main()
