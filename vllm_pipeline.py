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

    models = [
        ('llama3', 'meta-llama_Meta-Llama-3-8B-Instruct/'),
        ('codeLlama', 'meta-llama_CodeLlama-7b-hf/'),
        ('qwen', 'Qwen_Qwen1.5-7B-Chat/'),
        ('codeQwen', 'Qwen_CodeQwen1.5-7B-Chat/'),
        ('gemma', 'google_gemma-7b/'),
        ('mistral', 'mistralai_Mistral-7B-Instruct-v0.2/'),
        ('deepSeekCoder', 'deepseek-ai_deepseek-coder-6.7b-instruct/'),
    ]

    for model in models:
        model_name, model_path = model
        script2_command = f"python vllm_{experiment_name}.py --model-name {model_name} --model-path {model_path} --cuda-visible-devices {args.cuda_visible_devices}"
        script2_process = subprocess.Popen(script2_command, shell=True)
        script2_process.wait()
    
        print(f"Compmleted model inference for {model[0]}")

if __name__ == "__main__":
    main()
